import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.environ.get("BASE_PATH")) # type: ignore
from utils.visualization_utils import set_labels, highlight_max_bar, save_fig, COLORS

BASE_PATH = os.environ.get("BASE_PATH")
OUTPUT_DIR = f"{BASE_PATH}/outputs/bivariate_analysis"


def bivariate_analysis():
    print("bivariate analysis started...")
    df = pd.read_parquet(f"{BASE_PATH}/data/processed/df_final.parquet")
    df_sample = df.sample(frac=0.1, random_state=42)  # 10% = ~5.9M rows

    # --- is_snap column
    df_sample["is_snap"] = (
        ((df_sample["state_id"] == "CA") & df_sample["snap_CA"]) |
        ((df_sample["state_id"] == "TX") & df_sample["snap_TX"]) |
        ((df_sample["state_id"] == "WI") & df_sample["snap_WI"])
    )

    print("running sales overview plots...")
    # --- Total sales per state (pie)
    top_sales = df_sample.groupby("state_id")["sales"].sum()
    fig, ax = plt.subplots()
    plt.pie(x=top_sales, autopct="%1.1f%%", labels=top_sales.index, colors=COLORS)  # type: ignore
    plt.legend()
    save_fig(fig, f"{OUTPUT_DIR}/top_sales_per_state.png")

    # --- Top-selling item per store
    item_counts = (
        df_sample
        .groupby(["store_id", "item_id"])
        .size()
        .reset_index(name="sales")
    )
    top_item_per_store = (
        item_counts
        .sort_values("sales", ascending=False)
        .groupby("store_id")
        .first()
        .reset_index()
    )
    top_item_per_store["label"] = (
        top_item_per_store["store_id"].astype(str) + "  " + top_item_per_store["item_id"].astype(str)
    )
    fig, ax = plt.subplots()
    plt.barh(top_item_per_store["label"], top_item_per_store["sales"])
    set_labels("Top-Selling Item in Each Store", "Sales", "Store")
    save_fig(fig, f"{OUTPUT_DIR}/top_selling_item_per_store.png")

    # --- Total sales per store within each state
    state_store_sales = (
        df_sample
        .groupby(["state_id", "store_id"])["sales"]
        .sum()
        .reset_index()
    )
    fig, ax = plt.subplots(figsize=(12, 6))
    state_store_sales.pivot(index="state_id", columns="store_id", values="sales").plot(kind="bar", ax=ax)
    ax.legend(title="Store")
    set_labels("Total Sales per Store within Each State", "State", "Total Sales")
    save_fig(fig, f"{OUTPUT_DIR}/top_sales_within_state.png")

    # --- Total sales per category (pie)
    total_sales_per_category = df_sample.groupby("cat_id")["sales"].sum()
    fig, ax = plt.subplots()
    plt.pie(
        x=total_sales_per_category,
        autopct="%1.1f%%",
        labels=total_sales_per_category.index,  # type: ignore
        colors=COLORS
    )
    set_labels("Total Sales Per Each Category", "", "")
    plt.legend(loc="upper right")
    save_fig(fig, f"{OUTPUT_DIR}/total_sales_per_category.png")
    print("sales overview plots done.")

    print("running snap analysis...")
    # --- SNAP sales for FOODS per state
    food_snap_sales = (
        df_sample[(df_sample["cat_id"] == "FOODS") & df_sample["is_snap"]]
        .groupby("state_id")["sales"]
        .sum()
    )
    fig, ax = plt.subplots()
    sns.barplot(x=food_snap_sales.index, y=food_snap_sales.values, ax=ax)
    highlight_max_bar(ax)
    set_labels("FOODS Sales per State on SNAP Days", "State", "Total Sales")
    save_fig(fig, f"{OUTPUT_DIR}/food_snap_sales.png")

    # --- SNAP sales across all categories per state (pie)
    snap_sales = (
        df_sample[df_sample["is_snap"]]
        .groupby("state_id")["sales"]
        .sum()
    )
    fig, ax = plt.subplots()
    plt.pie(x=snap_sales, autopct="%1.1f%%", labels=snap_sales.index, colors=COLORS)  # type: ignore
    plt.legend(loc="upper right")
    save_fig(fig, f"{OUTPUT_DIR}/all_categories_snap_sales.png")
    print("snap analysis done.")

    print("running time analysis...")
    # --- Monthly sales trend
    monthly_sales = (
        df_sample
        .groupby(["year", "month"])["sales"]
        .sum()
        .reset_index()
    )
    monthly_sales["date"] = pd.to_datetime(monthly_sales[["year", "month"]].assign(day=1))
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(monthly_sales["date"], monthly_sales["sales"])
    set_labels("Monthly Sales Trend", "Date", "Total Sales")
    save_fig(fig, f"{OUTPUT_DIR}/monthly_trends_over_years.png")

    # --- Weekend vs Weekday sales
    weekend_sales = df_sample.groupby("is_weekend")["sales"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=weekend_sales, x="is_weekend", y="sales", ax=ax)
    set_labels("Weekend vs Weekday Sales", "Is Weekend", "Total Sales")
    save_fig(fig, f"{OUTPUT_DIR}/weekend_weekday_sales.png")

    # --- Highest sales per month
    monthly_by_name = df_sample.groupby("month")["sales"].sum().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=monthly_by_name, x="month", y="sales", ax=ax)
    plt.xticks(rotation=45)
    highlight_max_bar(ax)
    set_labels("Total Sales per Month", "Month", "Total Sales")
    save_fig(fig, f"{OUTPUT_DIR}/highest_sales_per_month.png")
    print("time analysis done.")

    print("running price analysis...")
    # --- Price change vs sales
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df_sample["price_change"], df_sample["sales"], alpha=0.3, s=5)
    set_labels("Price Change vs Sales", "Price Change", "Sales")
    save_fig(fig, f"{OUTPUT_DIR}/price_change_vs_sales.png")

    # --- Price relative to store vs sales
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df_sample["price_relative_to_store"], df_sample["sales"], alpha=0.3, s=5)
    set_labels("Price Relative to Store vs Sales", "Price Relative to Store", "Sales")
    save_fig(fig, f"{OUTPUT_DIR}/price_relative_to_store_vs_sales.png")
    print("price analysis done.")

    print("bivariate_analysis.py done")
    print(f"Checkout the new graphs in {OUTPUT_DIR}")


if __name__ == "__main__":
    bivariate_analysis()