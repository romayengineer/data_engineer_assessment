# data_engineer_assessment

## Build and run airflow service
```sh
# build docker images
docker compose build

# create tables for airflow
docker compose run --rm airflow-webserver airflow db migrate

# create admin user
docker compose run --rm airflow-webserver airflow users create \
  --username admin \
  --firstname Maxi \
  --lastname Admin \
  --role Admin \
  --email admin@example.com \
  --password admin

# start the services
docker compose up
```