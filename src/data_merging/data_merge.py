import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
def data_merge(): 
    # Load Data
    BASE_PATH = os.environ.get("BASE_PATH")
    calendar = pd.read_parquet(f"{BASE_PATH}/data/processed/calendar_cleaned.parquet")
    sales = pd.read_parquet(f"{BASE_PATH}/data/processed/sales_train_cleaned.parquet")
    price = pd.read_parquet(f"{BASE_PATH}/data/processed/sell_prices_cleaning.parquet")

    # Merging Sales days
    sales_long = pd.melt(
    sales,
    id_vars=["item_store_id", "item_id", "dept_id", "cat_id", "store_id", "state_id"],
    var_name="day_number",
    value_name="sales"
        )
    sales_long["day_number"] = sales_long["day_number"].astype("int16")

    # merge sales with calendar 
    sales_calendar = sales_long.merge(
    calendar, 
    on='day_number',
    how='left'
    )

    # merge sales_calendar with price
    df_merged = sales_calendar.merge(
    price,
    on=["store_id", "item_id", "walmart_year_week"],
    how="left"
    )

    # fill missing values
    df_merged['sell_price'] = df_merged['sell_price'].fillna(0)

    # Save Output
    output_path = os.path.join(BASE_PATH, 'data', 'processed', 'df_merged.parquet') # type: ignore
    df_merged.to_parquet(output_path, engine='pyarrow', index=False)
    print("merge.py: Done")
    print(f"Dataset Merged: {df_merged.shape[0]:,} rows, {df_merged.shape[1]} columns")
    print(f"Missing Valuse Count After Merging: {df_merged["sell_price"].isnull().sum()}")
