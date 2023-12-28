import subprocess
import tarfile
from datetime import datetime, timedelta
from os import environ

from minio import Minio
from prefect import flow, task
from tqdm import tqdm


@task
def dumpall(PG_PASSWORD, PG_URI, name="pg-export"):
    cmd = f"PGPASSWORD={PG_PASSWORD} pg_dumpall -d postgres://{PG_URI} > {name}.sql"
    print(f"Backing up {name} with command {cmd}")
    result = subprocess.run(cmd, shell=True, check=True)
    if result.returncode != 0:
        raise Exception("Error while dumping database: " + name + result.stderr)
    # check size... should be bigger than 1 mb
    with open(f"{name}.sql", "r") as f:
        if len(f.read()) < 1000:
            raise Exception("Dumped file is too small, something went wrong")


@task
def tar(name="pg-export"):
    with tarfile.open(f"{name}.sql.tar.gz", "w:gz") as tar:
        tar.add(f"{name}.sql")
    # remove .sql file
    subprocess.run(f"rm {name}.sql", shell=True)


@task
def uploadToS3(minioclient, name="pg-export"):
    minioclient.fput_object(
        environ["MINIO_BUCKET"],
        f"{name}-{datetime.utcnow().isoformat()}.sql.tar.gz",
        f"{name}.sql.tar.gz",
    )
    # delete local file
    subprocess.run(f"rm {name}.sql.tar.gz", shell=True)


@task
def deleteOldFiles(miniclient, keep_for_days: int = 30):
    fileByAge = dict()
    allFiles = miniclient.list_objects(environ["MINIO_BUCKET"])
    for file in allFiles:
        filename = file.object_name
        # split filename only at the first -
        _, date = filename.split("-", 1)
        # parse from isoformat
        date = datetime.fromisoformat(date[:-11])
        fileByAge[date] = filename
    for createdDate, filename in fileByAge.items():
        if createdDate < datetime.utcnow() - timedelta(days=keep_for_days):
            print(f"deleting {filename} bc older than {keep_for_days} days")
            miniclient.remove_object(environ["MINIO_BUCKET"], filename)


@flow(log_prints=True)
def backupAllDatabases():
    client = Minio(
        environ["MINIO_HOST"],
        access_key=environ["MINIO_USER"],
        secret_key=environ["MINIO_PASSWORD"],
        secure=True,
    )

    # the different URI and name combinations are submitted as ENV variable...
    # URI,NAME;URI2,NAME2;...
    databases = environ["DATABASES"].split(";")
    URIS = []
    for database in databases:
        URIS.append(database.split(","))
    failCount = 0
    for uri, name in tqdm(URIS):
        try:
            if "-" in name:
                raise ValueError("Name must not contain -")
            password = uri.split(":")[1].split("@")[0]
            dumpall(password, uri, name)
            tar(name)
            uploadToS3(client, name)
        except Exception as e:
            print(f"Error while backing up {name}: {e}")
            failCount += 1
            continue
    if failCount > 0:
        raise Exception(f"Backup finished with {failCount}/{len(databases)} errors")
    print("backup finished, deleting old files")
    deleteOldFiles(client, int(environ.get("KEEP_FOR_DAYS", 30)))


if __name__ == "__main__":
    backupAllDatabases()
