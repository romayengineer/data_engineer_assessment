import os

from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore
from datetime import datetime

from src.ingestion import load_csv
from src.dq import validate_rinde
from src.transform import to_parquet_partitioned
from src.config import CURATED_PATH


def ingest_task():
    return load_csv("rinde_lotes.csv")


def dq_task():
    df = load_csv("rinde_lotes.csv")
    validate_rinde(df)


def transform_task():
    df = load_csv("rinde_lotes.csv")
    output_path = os.path.join(CURATED_PATH, "rinde_lotes")
    to_parquet_partitioned(df, output_path)


with DAG(
    dag_id="csv_to_curated_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    ingest = PythonOperator(
        task_id="ingest_csv",
        python_callable=ingest_task,
    )

    dq = PythonOperator(
        task_id="data_quality_checks",
        python_callable=dq_task,
    )

    transform = PythonOperator(
        task_id="transform_to_parquet",
        python_callable=transform_task,
    )

    ingest >> dq >> transform
