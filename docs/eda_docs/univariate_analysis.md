## What's Actually Done in Univariate Analysis:
- load `df_merged.parquet` and sample 10% (~5.9M rows) with `random_state=42` for reproducibility.
- plot sales distribution and boxplot on non-zero sales only to avoid zero-inflation distortion.
- plot sell price distribution with x-axis limited to 0–60 to exclude extreme outliers.
- plot value counts for `cat_id`, `dept_id`, `store_id`, `state_id` as vertical barplots with highest bar highlighted.
- plot top 10 event names (excluding "No Event") as a horizontal barplot.
- save all plots to `outputs/univariate_analysis/`.
- print a message to user for ending this phase and saving plots to the desired output.

---

## Notes:
- 67.99% of sales records are zero — severe zero-inflation, sales filtered to non-zero before plotting distribution.
- sales distribution is heavily right-skewed with a long tail, max = 763.
- sell price ranges from 0 to 107.32, with 75% of prices below 4.97.
- all stores have approximately equal record counts (~591K–593K in sample).
- CA has the highest total records among states.
- "SuperBowl" is the most frequent event in the dataset.
- uses 10% sample via `df.sample(frac=0.1)` for memory efficiency on 16GB RAM.
- highest bar highlighted in red across all barplots via `highlight_max_bar()`.