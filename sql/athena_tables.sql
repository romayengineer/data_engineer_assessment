CREATE EXTERNAL TABLE IF NOT EXISTS curated.rinde_lotes (
    lote_id        string,
    campania       string,
    fecha          date,
    cultivo        string,
    superficie_ha. double,
    rinde_kg_ha    double,
    humedad_pct    double
)
PARTITIONED BY (
    campania string
)
STORED AS PARQUET
LOCATION 's3://bi-bucket/curated/rinde_lotes/';

CREATE EXTERNAL TABLE IF NOT EXISTS curated.clima_diario (
    lote_id           string,
    campania          string,
    fecha             date,
    temp_min_c        double,
    temp_max_c        double,
    precipitacion_mm  double
)
PARTITIONED BY (
    campania string
)
STORED AS PARQUET
LOCATION 's3://bi-bucket/curated/clima_diario/';
