## What's Actually Done in Price Features:
- load 5 columns from `df_merged.parquet`: `item_store_id`, `day_number`, `sell_price`, `sales`, `store_id`.
- sort by `item_store_id` then `day_number` to ensure correct temporal order.
- compute `price_change`: difference between current and previous day's sell price per `item_store_id`.
- compute `price_rolling_mean_4w`: mean of sell price over the past 4 weeks (28 days) per `item_store_id`.
- compute `price_relative_to_store`: sell price relative to the store's average sell price.
- save to `data/processed/price_features.parquet`.
---------------------------
## Notes:
- `.shift(1)` applied before rolling to avoid data leakage (excludes current day).
- first row per item will have `null` in `price_change`, first 4 rows in `price_rolling_mean_4w` — expected behavior.
- `price_change` captures promotional pricing signals (price drops → demand spikes).
- `price_rolling_mean_4w` captures medium-term pricing trend per item per store.
- `price_relative_to_store` captures how expensive/cheap an item is relative to its store's average.
- uses **polars** instead of pandas for memory efficiency on 59M rows.