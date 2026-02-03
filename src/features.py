import pandas as pd

def compute_rolling_slope(df: pd.DataFrame,window: int = 30) -> pd.DataFrame:
    
    df = df.copy()
    # compute per cycle change in smoothed capacity
    delta_capacity = (
        df.groupby("battery_id")["smooth_capacity"]
          .diff()
    )

    # smooth the slope with a rolling mean
    rolling_slope = (
        delta_capacity
        .groupby(df["battery_id"])
        .rolling(window=window, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )

    df["rolling_slope"] = rolling_slope
    return df