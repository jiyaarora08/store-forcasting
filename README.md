# Walmart M5 Sales Forecasting
> **DEPI Data Science Track | Team: DeepMetrix-**
> Predicting daily unit sales for 3,049 Walmart products across 10 stores using the [M5 Forecasting Kaggle dataset](https://www.kaggle.com/competitions/m5-forecasting-accuracy).

---

## Team
| Name | LinkedIn |
|------|----------|
| Youssef Moussa | [theyoussefmoussa](https://www.linkedin.com/in/theyoussefmoussa) |
| Malak Abdallah | [malak-abdallah](https://www.linkedin.com/in/malak-abdallah/) |
| Zyad Ashraf | [zyad-ashraff](https://www.linkedin.com/in/zyad-ashraff/) |
| Hamza Ahmed | [hamzaahmedamin](https://www.linkedin.com/in/hamzaahmedamin/) |
| Rahma Essam | [rahma-essam](https://www.linkedin.com/in/rahma-essam/) |
| Sara Mostafa | [sara--mostafa](https://www.linkedin.com/in/sara--mostafa/) |

---

## Current Milestone — Modeling
| Step | Status |
|------|--------|
| Data Collection | Done |
| Calendar Understanding | Done |
| Sales Train Understanding | Done |
| Sell Prices Understanding | Done |
| Calendar Cleaning | Done |
| Sales Train Cleaning | Done |
| Sell Prices Cleaning | Done |
| Merge & Validate | Done |
| Feature Engineering | Done |
| EDA | Done |
| Modeling | In Progress |
| Deployment | Upcoming |

---

## Project Structure
```
GRADUATION_PROJECT/
├── data/
│   ├── raw/
│   │   ├── calendar.csv
│   │   ├── sales_train_evaluation.csv
│   │   └── sell_prices.csv
│   └── processed/
│       ├── calendar_cleaned.parquet
│       ├── sales_train_cleaned.parquet
│       ├── sell_prices_cleaned.parquet
│       ├── df_merged.parquet
│       ├── time_features.parquet
│       ├── lag_features.parquet
│       ├── rolling_features.parquet
│       ├── price_features.parquet
│       └── df_final.parquet
│
├── notebooks/
│   ├── data_understanding/
│   │   ├── calendar_understanding.ipynb
│   │   ├── sales_train_understanding.ipynb
│   │   └── sell_prices_understanding.ipynb
│   ├── data_cleaning/
│   │   ├── calendar_cleaning.ipynb
│   │   ├── sales_train_cleaning.ipynb
│   │   └── sell_prices_cleaning.ipynb
│   ├── data_merging/
│   │   └── merge.ipynb
│   ├── feature_engineering/
│   │   ├── lag_features.ipynb
│   │   ├── time_features.ipynb
│   │   ├── rolling_features.ipynb
│   │   └── price_features.ipynb
│   └── eda/
│       ├── univariate_analysis.ipynb
│       └── bivariate_analysis.ipynb
│
├── src/
│   ├── data_cleaning/
│   │   ├── __init__.py
│   │   ├── calendar_cleaning.py
│   │   ├── sales_train_cleaning.py
│   │   └── sell_prices_cleaning.py
│   ├── data_merging/
│   │   ├── __init__.py
│   │   ├── data_merge.py
│   │   └── merge_final.py
│   ├── feature_engineering/
│   │   ├── __init__.py
│   │   ├── time_features.py
│   │   ├── lag_features.py
│   │   ├── rolling_features.py
│   │   └── price_features.py
│   └── eda/
│       ├── univariate_analysis.py
│       └── bivariate_analysis.py
│
├── utils/
│   ├── __init__.py
│   ├── cleaning_utils.py
│   ├── formatting.py
│   └── visualization_utils.py
│
├── docs/
│   ├── cleaning_docs/
│   │   ├── calendar_cleaning.md
│   │   ├── sales_train_cleaning.md
│   │   └── sell_prices_cleaning.md
│   ├── data_merging/
│   │   ├── merge.md
│   │   └── merge_final.md
│   ├── feature_engineering_docs/
│   │   ├── time_features.md
│   │   ├── lag_features.md
│   │   ├── rolling_features.md
│   │   └── price_features.md
│   └── eda_docs/
│       ├── univariate_analysis.md
│       └── bivariate_analysis.md
│
├── outputs/
│   ├── univariate_analysis/
│   │   ├── sales_distribution.png
│   │   ├── sell_price_distribution.png
│   │   ├── category_counts.png
│   │   ├── department_counts.png
│   │   ├── stores_counts.png
│   │   ├── state_counts.png
│   │   └── top_10_event_name.png
│   └── bivariate_analysis/
│       ├── top_sales_per_state.png
│       ├── top_selling_item_per_store.png
│       ├── top_sales_within_state.png
│       ├── total_sales_per_category.png
│       ├── food_snap_sales.png
│       ├── all_categories_snap_sales.png
│       ├── monthly_trends_over_years.png
│       ├── weekend_weekday_sales.png
│       ├── highest_sales_per_month.png
│       ├── price_change_vs_sales.png
│       └── price_relative_to_store_vs_sales.png
│
├── .gitignore
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## Datasets
| File | Rows | Cols | Description |
|------|------|------|-------------|
| `calendar.csv` | 1,969 | 14 | Daily calendar with events and SNAP flags |
| `sales_train_evaluation.csv` | 30,490 | 1,947 | Unit sales per item per day (wide format) |
| `sell_prices.csv` | ~6.8M | 4 | Weekly sell price per item per store |
| `df_merged.parquet` | ~59.2M | 18 | Merged long-format dataset ready for feature engineering |
| `time_features.parquet` | ~59.2M | 10 | `day_number`, `year`, `month`, `week`, `day`, `quarter`, `is_weekend`, `is_month_start`, `is_month_end` |
| `lag_features.parquet` | ~59.2M | 4 | `item_store_id`, `day_number`, `lag_7`, `lag_28` |
| `rolling_features.parquet` | ~59.2M | 5 | `item_store_id`, `day_number`, `rolling_mean_7`, `rolling_mean_28`, `rolling_std_7` |
| `price_features.parquet` | ~59.2M | 5 | `item_store_id`, `day_number`, `price_change`, `price_rolling_mean_4w`, `price_relative_to_store` |
| `df_final.parquet` | ~59.2M | 34 | Final dataset with all features merged, used for EDA and modeling |

---

## Setup & Usage
```bash
# 1. Clone the repo
git clone https://github.com/theyoussefmoussa/DeepMetrix-.git
cd DeepMetrix-

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup environment
cp .env.example .env
# edit .env and set BASE_PATH to your project path

# 4. Download the dataset from Kaggle
# https://www.kaggle.com/competitions/m5-forecasting-accuracy
# place the files in data/raw/

# 5. Run the pipeline
python3 main.py
```

---

## Dependencies
```
pandas>=2.0
numpy>=1.26
matplotlib>=3.8
seaborn>=0.13
python-dotenv==1.2.2
pyarrow>=14.0
polars>=1.42
lightgbm>=4.0
```

---

## Dataset Source
Kaggle — [M5 Forecasting - Accuracy](https://www.kaggle.com/competitions/m5-forecasting-accuracy)

---

## Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/theyoussefmoussa)
[![X](https://img.shields.io/badge/X-follow-black?style=for-the-badge&logo=x)](https://x.com/theyosefmusa)