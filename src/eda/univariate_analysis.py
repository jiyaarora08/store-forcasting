import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg") # to save plots without showing
import matplotlib.pyplot as plt
import sys
from utils.visualization_utils import set_labels
from utils.visualization_utils import highlight_max_bar, save_fig
import os 
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.environ.get("BASE_PATH")) # type: ignore
def univarite_analysis():
    BASE_PATH = os.environ.get("BASE_PATH")
    df = pd.read_parquet(f"{BASE_PATH}/data/processed/df_merged.parquet")
    df_sample = df.sample(frac=0.1, random_state=42)  # 10% = ~5.9M row
    OUTPUT_DIR = f"{BASE_PATH}/outputs/univariate_analysis"
    # Non Zero sales
    non_zero = df_sample[df_sample['sales'] > 0]['sales']

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    non_zero.plot(kind='hist', bins=50, ax=axes[0], title='Sales Distribution (Non-Zero)')
    non_zero.plot(kind='box', ax=axes[1], title='Sales Boxplot (Non-Zero)')
    save_fig(fig, output_path=f"{OUTPUT_DIR}/sales_distribution.png")

    # sell price distribution
    fig, ax = plt.subplots()
    ax.hist(df_sample['sell_price'], bins=50)
    ax.set_xlim(0, 60)
    ax.set_xticks(range(0, 61, 5))
    set_labels('Sell Price Distribution', 'Sell Price')
    save_fig(fig, f"{OUTPUT_DIR}/sell_price_distribution.png")

    # category counts
    cat_id_counts = df_sample['cat_id'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=cat_id_counts.index, y=cat_id_counts.values)
    highlight_max_bar(ax)
    set_labels('Category Counts', xlabel='Cateogry Name')
    save_fig(fig, f"{OUTPUT_DIR}/category_counts.png")

    # department counts
    dept_id_counts = df_sample['dept_id'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(
        x=dept_id_counts.index,
        y=dept_id_counts.values
    )
    set_labels(title='Departments', xlabel='department name')
    highlight_max_bar(ax)
    plt.xticks(rotation=45)
    save_fig(fig, f"{OUTPUT_DIR}/department_counts.png")

    # store_id counts
    store_counts = df_sample['store_id'].value_counts()
    fig, ax = plt.subplots()

    sns.barplot(
        x=store_counts.index,
        y=store_counts.values
    )
    highlight_max_bar(ax)
    set_labels(title='Stores Counts', xlabel='store')
    save_fig(fig,output_path=f"{OUTPUT_DIR}/stores_counts.png")

    # state counts
    state_counts = df_sample['state_id'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(
        x=state_counts.index,
        y=state_counts.values
    )
    highlight_max_bar(ax)
    plt.yticks(range(0, 2500000, 200000))
    set_labels("States", 'State name')
    save_fig(fig, f"{OUTPUT_DIR}/state_counts.png")

    # top 10 event names 
    event_name_counts = df_sample[df_sample['event_name'] != "No Event"]['event_name'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(
        x=event_name_counts.values,
        y=event_name_counts.index,
        ax=ax
    )
    highlight_max_bar(ax)
    set_labels("Top 10 Event Name Counts", xlabel="Count", ylabel="Event Name")
    save_fig(fig, f"{OUTPUT_DIR}/top_10_event_name.png")

    print(f"Checkout graphs in {OUTPUT_DIR}")
    print("univariate_analysis.py done") 
if __name__ == "__main__":
    univarite_analysis()