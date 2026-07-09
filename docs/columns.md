# Dataset Columns

Documentation of the three raw M5 Walmart sales forecasting files: `calendar.csv`, `sell_prices.csv`, and `sales_train_evaluation.csv`.

---

## calendar.csv

No missing values except `event_name_1`, `event_type_1`, `event_name_2`, `event_type_2` (see below).

| # | Column | Description |
|---|--------|-------------|
| 1 | `date` | Date in `yyyy-mm-dd` format. |
| 2 | `wm_yr_wk` | Walmart Year Week. Format: `111`02 → `111` is the Walmart year, `02` is the week within that year. Six Walmart years total: `111`–`116`. |
| 3 | `weekday` | Day of week as text, **starting from Saturday**. Value counts are roughly even across days (~281–282 each). |
| 4 | `wday` | Numeric encoding of `weekday` (Saturday = 1). |
| 5 | `month` | Month as integer, 1–12. |
| 6 | `year` | Year, 2012–2016. |
| 7 | `d` | Day index, `d_1` to `d_1969`. Extends 28 days beyond `sales_train_evaluation.csv`'s last day — that 28-day gap is the forecast horizon (see Notes). |
| 8 | `event_name_1` | Name of a calendar event on this date (e.g. Superbowl, Father's Day). Not a discount mechanism — discounts are handled separately via `snap_*`. **91.77% missing** (most days have no event). |
| 9 | `event_type_1` | Category of `event_name_1` (e.g. Cultural, National). |
| 10 | `event_name_2` | Second event on the same date, when applicable. **99.7% missing**. |
| 11 | `event_type_2` | Category of `event_name_2`. |
| 12 | `snap_CA` | Whether SNAP (Supplemental Nutrition Assistance Program / food stamps) benefits could be used this day in California. Binary. |
| 13 | `snap_TX` | Same as `snap_CA`, for Texas. |
| 14 | `snap_WI` | Same as `snap_CA`, for Wisconsin. |

---

## sell_prices.csv

No missing values.

| # | Column | Description |
|---|--------|-------------|
| 1 | `store_id` | Store identifier. 10 stores total: 4 in CA, 3 in TX, 3 in WI. |
| 2 | `item_id` | One of 3,049 items across `HOUSEHOLD`, `FOODS`, `HOBBIES` categories. |
| 3 | `wm_yr_wk` | Shared key with `calendar.csv`. |
| 4 | `sell_price` | Sell price for the item-store-week. Range: 0.01–107.32. |

---

## sales_train_evaluation.csv

No missing values.

| # | Column | Description |
|---|--------|-------------|
| 1 | `id` | Row identifier, e.g. `HOUSEHOLD_2_053_CA_2_evaluation`. 30,490 unique values (3,049 items × 10 stores). |
| 2 | `item_id` | Shared key with `sell_prices.csv`, e.g. `HOBBIES_1_001` = category name + category number + unique item identifier. |
| 3 | `dept_id` | Department identifier: `HOBBIES_1`, `HOBBIES_2`, `HOUSEHOLD_1`, `HOUSEHOLD_2`, `FOODS_1`, `FOODS_2`, `FOODS_3`. Encodes `cat_id` as a prefix (redundant with column 4 — worth keeping in mind when selecting categorical features for modeling). |
| 4 | `cat_id` | Category identifier: `FOODS`, `HOUSEHOLD`, `HOBBIES`. |
| 5 | `store_id` | Store identifier, 10 stores, shared key with `sell_prices.csv`. |
| 6 | `state_id` | State identifier: `CA`, `TX`, `WI`. |
| 7 | `d_1` ... `d_1946` | Daily unit sales per row, one column per day. |

---

## Notes

- **Day range gap**: `calendar.csv` covers `d_1`–`d_1969`; `sales_train_evaluation.csv` covers `d_1`–`d_1946`. The 28-day difference is the held-out forecast horizon — `calendar.csv` is intentionally longer since it provides date features needed for the days being predicted.
- **Cross-file key consistency** (validated):
  - `wm_yr_wk` values present in `sell_prices.csv` but missing from `calendar.csv`: **0**
  - `(item_id, store_id)` combinations in `sales_train_evaluation.csv` with zero price history in `sell_prices.csv`: **0**