import subprocess
import tarfile
from datetime import datetime
from os import environ

from minio import Minio
from prefect import flow, task


@task
def dumpall(PG_PASSWORD, PG_URI, name="pg-export"):
    cmd = f"PGPASSWORD={PG_PASSWORD} pg_dumpall -d postgres://{PG_URI} > {name}.sql"
    subprocess.run(cmd, shell=True)


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
    for uri, name in URIS:
        try:
            password = uri.split(":")[1].split("@")[0]
            print(f"Backing up {name} with uri {uri}")
            dumpall(password, uri, name)
            tar(name)
            uploadToS3(client, name)
        except Exception as e:
            print(f"Error while backing up {name}: {e}")
            continue
