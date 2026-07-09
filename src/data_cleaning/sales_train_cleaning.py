import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
from src.data_cleaning.load_data import load_data

def sales_train_cleaning(): 
    BASE_PATH = os.environ.get("BASE_PATH")
    file_path = f'{BASE_PATH}/data/raw/sales_train_evaluation.csv'
    sales = load_data(file_path)
    # Memory Usage
    print(f"Before Cleaning Sales Train: {sales.memory_usage(deep=True).sum() / 1e6:.1f} MB")

    # Strip d_days and downcast datatype
    sales.columns = sales.columns.str.replace(r'^d_', '', regex=True)
    cols = sales.columns[sales.columns.str.isnumeric()]
    sales[cols] = sales[cols].astype('Int16')

    # rename id for better readability
    sales.rename(columns={'id' : 'item_store_id'}, inplace=True)

    # converting columns to category
    str_cols = ['dept_id', 'cat_id', 'store_id', 'state_id', 'item_id']
    for col in str_cols: 
        sales[col] = sales[col].astype('category')

    print(f"After Cleaning Sales Train: {sales.memory_usage(deep=True).sum() / 1e6:.1f} MB")

    # Save to parquet
    output_path = os.path.join(BASE_PATH, 'data', 'processed', 'sales_train_cleaned.parquet') # type: ignore
    sales.to_parquet(output_path, engine='pyarrow', index=False)
    print("sales_train_cleaning.py: Done")
    print(f"Sales Train Cleaned: {sales.shape[0]:,} rows, {sales.shape[1]} columns")