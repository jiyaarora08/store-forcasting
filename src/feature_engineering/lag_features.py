import polars as pl
import os
from dotenv import load_dotenv
load_dotenv()
def lag_features():
    BASE_PATH = os.environ.get("BASE_PATH")
    df = pl.read_parquet(
        f"{BASE_PATH}/data/processed/df_merged.parquet",
        columns=["item_store_id", "day_number", "sales"]
    )

    df = df.sort(["item_store_id", "day_number"])

    df = df.with_columns([
        pl.col("sales").shift(7).over("item_store_id").alias("lag_7"),
        pl.col("sales").shift(28).over("item_store_id").alias("lag_28"),
    ])
    df = df.drop('sales')

    print(f"Lag Features Shape: {df.shape}")
    print(f"Memory Usage: {df.estimated_size('mb'):.1f} MB")

    output_path = f"{BASE_PATH}/data/processed/lag_features.parquet"
    df.write_parquet(output_path)
    print("lag_features.py: Done")


if __name__ == "__main__":
    lag_features()