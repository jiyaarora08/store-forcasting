import polars as pl
import os
from dotenv import load_dotenv
load_dotenv()
BASE_PATH = os.environ.get("BASE_PATH")
PROCESSED = f"{BASE_PATH}/data/processed"


def final_merge():
    print("final_merge started...")

    print("loading df_merged...")
    df = pl.read_parquet(f"{PROCESSED}/df_merged.parquet")
    df = df.sort(["item_store_id", "day_number"])
    print(f"df_merged loaded: {df.shape}")

    print("adding time features...")
    df = df.with_columns([
        pl.col("date").dt.year().cast(pl.Int16).alias("year"),
        pl.col("date").dt.month().cast(pl.Int16).alias("month"),
        pl.col("date").dt.week().cast(pl.Int16).alias("week"),
        pl.col("date").dt.day().cast(pl.Int16).alias("day"),
        pl.col("date").dt.quarter().cast(pl.Int16).alias("quarter"),
        (pl.col("date").dt.weekday() >= 5).alias("is_weekend"),
        pl.col("date").dt.month_start().alias("is_month_start"),
        pl.col("date").dt.month_end().alias("is_month_end"),
    ])
    print("time features done.")

    print("adding lag features...")
    df = df.with_columns([
        pl.col("sales").shift(7).over("item_store_id").alias("lag_7"),
        pl.col("sales").shift(28).over("item_store_id").alias("lag_28"),
    ])
    print("lag features done.")

    print("adding rolling features...")
    df = df.with_columns([
        pl.col("sales").shift(1).rolling_mean(7).over("item_store_id").alias("rolling_mean_7"),
        pl.col("sales").shift(1).rolling_mean(28).over("item_store_id").alias("rolling_mean_28"),
        pl.col("sales").shift(1).rolling_std(7).over("item_store_id").alias("rolling_std_7"),
    ])
    print("rolling features done.")

    print("adding price features...")
    df = df.with_columns([
        (pl.col("sell_price") - pl.col("sell_price").shift(1)).over("item_store_id").alias("price_change"),
        pl.col("sell_price").shift(1).rolling_mean(4).over("item_store_id").alias("price_rolling_mean_4w"),
        (pl.col("sell_price") / pl.col("sell_price").mean().over("store_id")).alias("price_relative_to_store"),
    ])
    print("price features done.")

    print(f"df_final shape: {df.shape}")
    print(f"memory usage: {df.estimated_size('mb'):.1f} MB")

    df.write_parquet(f"{PROCESSED}/df_final.parquet")
    print(f"df_final.parquet saved.")
    print("final_merge.py done.")


if __name__ == "__main__":
    final_merge()