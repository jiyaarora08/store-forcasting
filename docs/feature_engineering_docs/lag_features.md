## What's Actually Done in Lag Features:
- load 3 columns from `df_merged.parquet`: `item_store_id`, `day_number`, `sales`.
- sort by `item_store_id` then `day_number` to ensure correct temporal order.
- compute `lag_7`: sales value from 7 days ago per `item_store_id`.
- compute `lag_28`: sales value from 28 days ago per `item_store_id`.
- save to `data/processed/lag_features.parquet`.
---------------------------
## Notes:
- lag is computed per `item_store_id` using `.over()` to avoid leakage across items.
- first 7 rows per item will have `null` in `lag_7`, first 28 rows in `lag_28` — expected behavior.
- uses **polars** instead of pandas for memory efficiency on 59M rows.
- `lag_7` captures same-day-of-week pattern from last week (weekly seasonality).
- `lag_28` captures same-day pattern from last month (monthly seasonality).