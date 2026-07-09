## What's Actually Done in final_merge:
- load `df_merged.parquet` (59M rows × 18 columns) using Polars.
- sort by `["item_store_id", "day_number"]` to ensure correct lag and rolling calculations.
- add time features directly: `year`, `month`, `week`, `day`, `quarter`, `is_weekend`, `is_month_start`, `is_month_end` from the `date` column.
- add lag features: `lag_7`, `lag_28` using `shift()` over `item_store_id`.
- add rolling features: `rolling_mean_7`, `rolling_mean_28`, `rolling_std_7` using `shift(1).rolling_mean/std()` over `item_store_id`.
- add price features: `price_change`, `price_rolling_mean_4w`, `price_relative_to_store` using `shift()` and `mean()` over `item_store_id` and `store_id`.
- save final result as `df_final.parquet` (59M rows × 34 columns) to `data/processed/`.

---

## Problems Faced:

**Approach 1 — join separate feature parquets:**
- loaded `df_merged`, `lag_features`, `rolling_features`, `price_features`, `time_features` all at once then joined them.
- crashed during the join phase — total RAM required exceeded 16GB:
    - `lag_features` → 1975 MB in memory
    - `rolling_features` → 3110 MB in memory
    - `price_features` → 2426 MB in memory
    - `df_merged` → ~4-5 GB in memory
- total: **+10 GB before the join even starts**.

**Approach 2 — chunk-based join:**
- loaded feature parquets once, then split `df_merged` into 5M-row chunks and joined each chunk separately.
- still crashed — feature parquets alone consumed too much RAM before any chunk processing started.

**Approach 3 (final) — compute features directly on `df_merged`:**
- load only `df_merged` once (~294 MB on disk).
- compute all features in-place using `with_columns()` — no extra DataFrames in memory.
- peak memory: **8585 MB** — within 16GB limit.
- `df_final.parquet` saved successfully: **59M rows × 34 columns**.

---

## Notes:
- all feature engineering previously done in separate scripts (`lag_features.py`, `rolling_features.py`, `price_features.py`, `time_features.py`) is now consolidated here for memory efficiency.
- separate feature parquets are still kept for reference but are no longer used in the pipeline after this point.
- `df_final.parquet` is the single source of truth for both EDA (bivariate analysis) and the modeling phase.
- Polars used instead of pandas for memory efficiency on 59M rows with 16GB RAM.
- `with_columns()` in Polars computes features lazily within the same DataFrame without duplicating memory.