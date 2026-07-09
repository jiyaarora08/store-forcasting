## What I want to do:
1. rename columns to be more readable
2. replace the underscore and convert to int, for example d_100 to 100
3. convert date to datetime instead of str and the format yyyy-mm-dd
4. remove event_name_2 and event_type_2 columns (99.7% missing)
5. check for duplicates & redundant columns
6. fill missing values in event_name_1 and event_type_1 with `No Event`
7. downcasting datatypes for better memory optimization.


-------------------------------
## What's Actually Done
- rename columns to be more readable
- change `date` to datetime instead of str
- Redundant Columns: wday have the same value as weekday, drop wday cause `weekday` is easy to read and will be used for encoding.
- converting `weekay` to category instead of str.
- Dropping columns: event_name_2 & event_type_2
- convert `month` to `month_name` with mapping, converting it to category.
- replace d_ with empty space in day_number d_1500: 1500, and change datatype to 'int16'
- fill missing values in `event_type` & `event_name` with 'no_event' the function will be added to utils/
- converting datatypes of `event_type` & `event_name` to category
- converting `snap_TX`, `snap_CA`, `snap_WI` datatype to bool.
- droping `year` column after validating it's the same as years in `date` column (Temporary extracting it for validating)
- saving the output in date/processed/calendar_cleaned.parquet

