## What's Actually Done in Sales Train: 
- calculate memory usage before cleaning (476.8 MB).
- strip prefix and downcast to int16 for d_days.
- rename `id` to `item_store_id`
- converting `dept_id` to category.
- converting `cat_id` to category.
- converting `store_id` to category.
- converting `state_id` to category.
- converting `item_id` to category
- calculate memory usage after cleaning (178 MB).
---------------------------
## Notes: 
- `item_store_id` has 30490 unique values.
- `item_id` has 3049 unique values.