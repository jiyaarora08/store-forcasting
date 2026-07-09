import os
import pandas as pd

from src.data_cleaning.load_data import load_data
from utils.cleaning_utils import fill_missing
from dotenv import load_dotenv
load_dotenv()

def calendar_cleaning():
    BASE_PATH = os.environ.get("BASE_PATH")
    file_path = f'{BASE_PATH}/data/raw/calendar.csv'
    calendar = load_data(file_path)
    # Renaming columns for readability
    calendar.rename(columns={
        'd': 'day_number',
        'event_name_1': 'event_name',
        'event_type_1': 'event_type',
        'wm_yr_wk': 'walmart_year_week'
    }, inplace=True)

    # Convert date to datetime
    calendar['date'] = pd.to_datetime(calendar['date'])

    # Drop redundant and validated columns
    calendar.drop(columns=['wday', 'year', 'event_name_2', 'event_type_2'], inplace=True)

    # Downcast walmart_year_week
    calendar['walmart_year_week'] = calendar['walmart_year_week'].astype('int32')

    # Month name from date
    calendar['month_name'] = calendar['date'].dt.month_name()
    calendar.drop(columns=['month'], inplace=True)

    # day_number: strip prefix and downcast
    calendar['day_number'] = calendar['day_number'].str.replace('d_', '').astype('int16')

    # Fill missing event columns
    event_cols = ['event_type', 'event_name']
    calendar = fill_missing(calendar, 'No Event', event_cols)

    # Dtype conversions
    for col in event_cols:
        calendar[col] = calendar[col].astype('category')

    calendar['weekday'] = calendar['weekday'].astype('category')
    calendar['month_name'] = calendar['month_name'].astype('category')

    for col in ['snap_CA', 'snap_TX', 'snap_WI']:
        calendar[col] = calendar[col].astype(bool)

    # Save to parquet
    output_path = os.path.join(BASE_PATH, 'data', 'processed', 'calendar_cleaned.parquet') # type: ignore
    calendar.to_parquet(output_path, engine='pyarrow', index=False)
    print("calendar_cleaning.py: Done")
    print(f"Calendar Cleaned: {calendar.shape[0]:,} rows, {calendar.shape[1]} columns")


if __name__ == "__main__":
    calendar_cleaning()