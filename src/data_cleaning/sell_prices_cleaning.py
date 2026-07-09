import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
from src.data_cleaning.load_data import load_data
def sell_prices_cleaning():
    # load data
    BASE_PATH  = os.environ.get("BASE_PATH")
    file_path = f'{BASE_PATH}/data/raw/sell_prices.csv'
    price = load_data(file_path)

    print(f"Before Cleaning Sell Prices: {price.memory_usage(deep=True).sum() / 1e6:.1f} MB")

    # renaming columns 
    price.rename(columns={'wm_yr_wk' : 'walmart_year_week'}, inplace=True)

    # converting to category
    str_cols = ['store_id', 'item_id']
    for col in str_cols: 
        price[col] = price[col].astype('category')

    # converting walmart_year_week to int32
    price['walmart_year_week'] = price['walmart_year_week'].astype('int32')

    # converting sell prices to float 32
    price['sell_price'] = price['sell_price'].astype('float32')

    # save the output
    output_path = os.path.join(BASE_PATH, 'data', 'processed', 'sell_prices_cleaning.parquet') # type: ignore
    price.to_parquet(output_path, engine='pyarrow', index=False)
    print(f"After Cleaning Sell Prices: {price.memory_usage(deep=True).sum() / 1e6:.1f} MB")
    print("sell_prices_cleaning.py: Done")
    print(f"Sell Prices Cleaned: {price.shape[0]:,} rows, {price.shape[1]} columns")
