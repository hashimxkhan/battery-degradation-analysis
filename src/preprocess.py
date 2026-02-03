import pandas as pd

def normalize_capacity(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize capacity per battery
    df = df.copy()

    # Get initial capacity per battery
    initial_capacity = (
        df.groupby("battery_id")["BCt"]
        .transform("first")
    )

    df["norm_capacity"] = df["BCt"] / initial_capacity
    return df


def smooth_capacity( df: pd.DataFrame, window: int = 30) -> pd.DataFrame:
    # compute rolling mean
    df = df.copy()
    
    rolling_mean = (
        df.groupby("battery_id")["norm_capacity"]
          .rolling(window=window, min_periods=1)
          .mean()
          .reset_index(level=0, drop=True)
    )
    
    df["smooth_capacity"] = rolling_mean
    return df

def preprocess(df: pd.DataFrame, window: int = 30) -> pd.DataFrame:
    df = normalize_capacity(df)
    df = smooth_capacity(df, window=window)
    return df