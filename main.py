from src.load_data import load_battery_data
from src.plots import plot_raw_capacity, plot_raw_vs_smoothed, plot_rolling_slope
from src.preprocess import preprocess
from src.features import compute_rolling_slope
import pandas as pd

path = "data/battery_dataset.csv"

def main():
    df = load_battery_data(path)
    plot_raw_capacity(df)
    df = preprocess(df, window=30)
    plot_raw_vs_smoothed(df)
    df = compute_rolling_slope(df, window=30)

    pd.set_option('display.max_rows', None)
    print(df[["battery_id", "cycle", "rolling_slope"]])
    plot_rolling_slope(df)

if __name__ == "__main__":
    main()