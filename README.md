# Cloud Data Engineer Assessment – CSV to Curated Pipeline (Airflow + Athena)

This project implements a complete **data ingestion + validation + transformation pipeline** for an agricultural analytics use case.

The goal is to ingest two CSV datasets:

- `rinde_lotes.csv` (crop yield per lot)
- `clima_diario.csv` (daily weather observations)

Then process them into a curated Parquet layer partitioned by campaign and lot, validate data quality rules, and expose an Athena-ready BI view.

## ✅ Project Features

- Synthetic CSV data generator (realistic schema + join keys)
- Modular ETL pipeline in Python:
  - ingestion
  - data quality checks
  - transformation + curated load
- Orchestration with Apache Airflow
- Local execution using Docker Compose
- Athena SQL scripts for external tables + BI view

## 📂 Project Structure

```

data_engineer_assessment/
│
├── dags/
│   └── ingestion_pipeline.py        # Airflow DAG definition
│
├── src/
│   ├── ingestion.py                # CSV ingestion logic
│   ├── dq.py                       # Data quality validations
│   ├── transform.py                # Parquet + partitioning
│   └── config.py                   # Shared paths/config
│
├── data/
│   ├── rinde_lotes.csv              # Generated sample dataset
│   └── clima_diario.csv             # Generated sample dataset
│
├── sql/
│   ├── athena_tables.sql            # CREATE EXTERNAL TABLE statements
│   ├── athena_partitions.sql        # MSCK REPAIR TABLE commands
│   └── bi_view.sql                  # BI view combining yield + climate
│
├── scripts/
│   └── generate_data.py             # Script to generate realistic CSVs
│
├── Dockerfile                       # Airflow image with dependencies
├── docker-compose.yml               # Local Airflow stack
├── requirements.txt
└── README.md

```

---

## 🚀 Pipeline Overview

The Airflow DAG executes the following steps:

1. **Ingest CSV**
   - Reads raw CSV files into DataFrames

2. **Data Quality Checks**
   Validations include:
   - yield range checks
   - null percentage thresholds
   - date consistency

3. **Transform + Curated Load**
   - Converts datasets into Parquet
   - Writes them partitioned by:
     - `campania`
     - `lote_id`

4. **Athena / BI Layer**
   - SQL scripts define Athena external tables
   - A BI view joins yield + climate for analytics

---

## 🧪 Synthetic Data Generation

Since the original CSVs were not provided, this project includes a generator:

```bash
python scripts/generate_data.py
```

It produces:

* realistic crop yield values (`rinde_kg_ha`)
* daily weather metrics (temperature, rainfall, humidity)
* consistent join keys (`campania`, `lote_id`, `fecha`)

---

## 🛠️ Running Airflow Locally (Docker Compose)

### 1. Build and start services


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

---

### Access the Airflow UI

Open:

[http://localhost:8080](http://localhost:8080)

### Trigger the DAG

In the UI:

* Enable DAG `csv_to_curated_pipeline`
* Click **Trigger DAG**

---

## 📌 Airflow DAG Design

The DAG is defined in:

```
dags/ingestion_pipeline.py
```

It imports modular task logic from `src/`:

* `src.ingestion.load_csv`
* `src.dq.validate_rinde`
* `src.transform.to_parquet_partitioned`

This keeps the DAG lightweight and production-ready.

---

## 📊 Athena SQL Layer

All Athena queries are stored under:

```
sql/
```

### Includes:

* External table definitions
* Partition repair commands
* BI analytics view:

This view enriches yield results with weather aggregates (30 days before harvest).

---

## 🔒 Security & Best Practices

* Airflow services share a common `SECRET_KEY`
* No heavy computation occurs at DAG parse/import time
* Partitioning improves Athena query performance
* Modular code layout supports testing and scalability

---

## 📈 Cost & Performance Notes

* Parquet format reduces storage + Athena scan cost
* Partitioning by campaign and lot improves query pruning
* In real production, ingestion could be extended with:

  * AWS Glue
  * EMR/Spark
  * Lake Formation permissions

---

## ✅ Deliverables Covered

✔ Modular Python repo + tests
✔ Airflow DAG orchestration
✔ Data Quality validations
✔ Curated Parquet layer in S3-style layout
✔ Athena external tables + BI view scripts
✔ README with performance + security notes
