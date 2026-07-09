## What's Actually Done in Time Features:
- load 5 columns from `df_merged.parquet`: `date`, `day_number`, `walmart_year_week`, `month_name`, `weekday`.
- extract `year`, `month`, `week`, `day`, `quarter` from `date`.
- extract `is_weekend` from `date` (Saturday=5, Sunday=6).
- extract `is_month_start` and `is_month_end` from `date`.
- downcast `year`, `month`, `day`, `quarter` to int16.
- drop `date` column after extraction.
- save to `data/processed/time_features.parquet`.
---------------------------
## Notes:
- `month_name` and `weekday` are kept from calendar cleaning as category dtype.
- `is_weekend` is derived from `dayofweek` not `day` (Monday=0, Sunday=6).