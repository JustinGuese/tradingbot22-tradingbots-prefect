implementing my tradingbot ideas as prefect flows, being executed in a docker container running on my caprover server, connecting to the tradingbot backend via internal network routing

ci/cd done with caprover

schedule and names in [flows/addAllFlows.py](flows/addAllFlows.py)

needs little persistence at /app/persistent/


## database backup function

[flows/databaseBackup.py](flows/databaseBackup.py) backs up postfres databases to a minio destination. it deletes files older than 30 d.
restore is possible with

```bash
tar -xvf pg_tradingbot-2023-12-28T14_04_58.128214.sql.tar.gz
psql -h 10.1x.x.x -p 5432 -U postgres < pg_tradingbot.sql
```