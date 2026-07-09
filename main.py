from src.data_cleaning.calendar_cleaning import calendar_cleaning
from src.data_cleaning.sales_train_cleaning import sales_train_cleaning
from src.data_cleaning.sell_prices_cleaning import sell_prices_cleaning
from src.data_merging.data_merge import data_merge
from utils.formatting import separator
from src.feature_engineering.time_features import time_features
from src.feature_engineering.lag_features import lag_features
from src.feature_engineering.rolling_features import rolling_features
from src.feature_engineering.price_features import price_features
from src.eda.univariate_analysis import univarite_analysis
from src.eda.bivariate_analysis import bivariate_analysis
from src.data_merging.final_merge import final_merge
from src.modeling.lightgbm_model import lightgbm_model

if __name__ == "__main__":
    separator(title='Calendar Cleaning')
    calendar_cleaning()
    separator(title='Sales Train Cleaning')
    sales_train_cleaning()
    separator(title='Sell Prices Cleaning')
    sell_prices_cleaning()
    separator(title='Data Merging')
    data_merge()
    separator(title="Time Features")
    time_features()
    separator(title='Lag Features')
    lag_features()
    separator(title='Rolling Features')
    rolling_features()
    separator(title='Price Features')
    price_features()
    separator("Final Merge")
    final_merge()
    separator("EDA: Univariate Analysis")
    univarite_analysis()
    separator("EDA: Bivariate Analysis")
    bivariate_analysis()
    separator("Modeling: LightGBM")
    lightgbm_model()