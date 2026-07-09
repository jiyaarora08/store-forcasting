## What's Actually Done in Bivariate Analysis:
- load `df_merged.parquet` and sample 10% (~5.9M rows) with `random_state=42` for reproducibility.
- merge `time_features.parquet` on `day_number` and `price_features.parquet` on `["item_store_id", "day_number"]` upfront into a single `df_sample`.
- compute `is_snap` column per row based on state-specific SNAP flags (`snap_CA`, `snap_TX`, `snap_WI`).
- plot total sales per state as a pie chart.
- plot top-selling item per store as a horizontal barplot (ranked by row count per `store_id` + `item_id`).
- plot total sales per store within each state as a grouped barplot.
- plot total sales per category as a pie chart.
- plot FOODS sales per state on SNAP days as a barplot with highest bar highlighted.
- plot total sales per state on SNAP days across all categories as a pie chart.
- plot monthly sales trend over the years as a line chart using `year` + `month` from `time_features`.
- plot weekend vs weekday total sales as a barplot using `is_weekend` from `time_features`.
- plot total sales per month by name as a barplot with highest bar highlighted.
- plot price change vs sales as a scatter plot using `price_change` from `price_features`.
- plot price relative to store vs sales as a scatter plot using `price_relative_to_store` from `price_features`.
- save all plots to `outputs/bivariate_analysis/`.
- print section-level messages to terminal to confirm progress across 4 stages: sales overview, snap analysis, time analysis, price analysis.

---

## Notes:
- all merges done once at the top to avoid redundant DataFrames (`result`, `price_result`) in memory.
- `time_features` deduplicated on `day_number` before merge; `price_features` deduplicated on `["item_store_id", "day_number"]`.
- duplicate columns from merge (`walmart_year_week_y`, `month_name_y`, `weekday_y`, `date`) dropped and `_x` suffixes renamed after merge.
- `is_snap` is state-aware — each row checks the SNAP flag of its own state, not all states combined.
- top-selling item per store is based on row count (number of days the item appeared), not sum of sales — reflects item presence frequency.
- monthly trend uses `pd.to_datetime` on `year` + `month` columns to construct a proper date axis.
- uses 10% sample via `df.sample(frac=0.1)` for memory efficiency on 16GB RAM.
- highest bar highlighted in red across all barplots via `highlight_max_bar()`.