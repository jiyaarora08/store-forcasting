from pathlib import Path
import pandas as pd
def load_data(file_path: str | Path):
    df = pd.read_csv(file_path)
    print(f"Loaded: {df.shape[0]:,} rows, {df.shape[1]} columns")
    return df