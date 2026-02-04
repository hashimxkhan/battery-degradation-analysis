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


def compute_curvature(df: pd.DataFrame,min_cycle: int = 60) -> pd.DataFrame:

    df = df.copy()
    curvature = (
        df.groupby("battery_id")["rolling_slope"]
          .diff()
    )

    df["curvature"] = curvature
    # Mask out first 60 cycles to facilitate rolling window
    df.loc[df["cycle"] < min_cycle, "curvature"] = pd.NA

    return df

def detect_persistent_acceleration(df: pd.DataFrame, curvature_threshold: float = -1e-5, persistence_window: int = 10
                                   ) -> pd.DataFrame:

    df = df.copy()
    # Acceleration condition
    accel = df["curvature"] < curvature_threshold

    # Require persistence
    persistent = (
        accel
        .groupby(df["battery_id"])
        .rolling(window=persistence_window, min_periods=1)
        .sum()
        .reset_index(level=0, drop=True)
        >= persistence_window
    )

    df["persistent_accel"] = persistent
    return df