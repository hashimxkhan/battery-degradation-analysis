import pandas as pd

REQUIRED_COLUMNS = {"battery_id","cycle","BCt"}

def load_battery_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    # validate dataset
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    # drop any rows that have null values for required columns
    df = df[list(REQUIRED_COLUMNS)].dropna()
    
    return df