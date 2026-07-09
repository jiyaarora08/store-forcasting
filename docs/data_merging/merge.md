## What's Actually Done in Merge & Validate:
- load three cleaned parquet files: `calendar_cleaned`, `sales_train_cleaned`, `sell_prices_cleaned`.
- melt `sales_train_cleaned` from wide format (30,490 × 1,947) to long format (59,181,090 × 8).
- cast `day_number` from string to int16 after melt.
- merge `sales_long` with `calendar_cleaned` on `day_number` (left join) → (59,181,090 × 17).
- merge result with `sell_prices_cleaned` on `store_id` + `item_id` + `walmart_year_week` (left join) → (59,181,090 × 18).
- fill missing values in `sell_price` with 0.
- validate row count after each merge step.
- save final merged dataset to `data/processed/df_merged.parquet`.
---------------------------
## Notes:
- `sell_price` has ~12,299,413 nulls — expected, not every item has a price for every week.
- null handling for `sell_price` is deferred to feature engineering (planned: forward fill per `store_id` + `item_id`).
- all merges are left joins to preserve all 59,181,090 rows.