import os

def to_parquet_partitioned(df, output_path):
    os.makedirs(output_path, exist_ok=True)

    df.to_parquet(
        output_path,
        engine="pyarrow",
        partition_cols=["campaña", "lote_id"],
        compression="snappy"
    )
