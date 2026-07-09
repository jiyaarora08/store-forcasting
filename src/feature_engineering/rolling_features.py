import polars as pl
import os
from dotenv import load_dotenv
load_dotenv()
def rolling_features():
    BASE_PATH = os.environ.get("BASE_PATH")
    df = pl.read_parquet(
            f"{BASE_PATH}/data/processed/df_merged.parquet",
            columns=["item_store_id", "day_number", "sales"]
        )
    
    df = df.sort(["item_store_id", "day_number"])
    
    # rolling within one week
    df = df.with_columns([
        pl.col("sales").shift(1).rolling_mean(7).over("item_store_id").alias("rolling_mean_7"),
        pl.col('sales').shift(1).rolling_mean(28).over('item_store_id').alias('rolling_mean_28'), # rolling within monthly (montly trending)
        pl.col('sales').shift(1).rolling_std(7).over('item_store_id').alias('rolling_std_7'), 
    ])
    df = df.drop("sales")
    print(f"Rolling Features Shape: {df.shape}")
    print(f"Memory Usage: {df.estimated_size('mb'):.1f} MB")

    output_path = f"{BASE_PATH}/data/processed/rolling_features.parquet"
    df.write_parquet(output_path)
    print("rolling_features.py: Done")


if __name__ == "__main__":
    rolling_features()