## What's Actually Done in Rolling Features:
- load 3 columns from `df_merged.parquet`: `item_store_id`, `day_number`, `sales`.
- sort by `item_store_id` then `day_number` to ensure correct temporal order.
- compute `rolling_mean_7`: mean of sales over the past 7 days per `item_store_id`.
- compute `rolling_mean_28`: mean of sales over the past 28 days per `item_store_id`.
- compute `rolling_std_7`: standard deviation of sales over the past 7 days per `item_store_id`.
- save to `data/processed/rolling_features.parquet`.
---------------------------
## Notes:
- `.shift(1)` applied before rolling to avoid data leakage (excludes current day).
- first 7 rows per item will have `null` in `rolling_mean_7` and `rolling_std_7`, first 28 rows in `rolling_mean_28` — expected behavior.
- uses **polars** instead of pandas for memory efficiency on 59M rows.
- `rolling_mean_7` captures short-term weekly trend.
- `rolling_mean_28` captures monthly trend (4 weeks = 28 days).
- `rolling_std_7` captures sales volatility over the past week.