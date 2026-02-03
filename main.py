from src.load_data import load_battery_data
from src.plots import plot_raw_capacity, plot_raw_vs_smoothed
from src.preprocess import preprocess

path = "data/battery_dataset.csv"

def main():
    df = load_battery_data(path)
    plot_raw_capacity(df)
    df = preprocess(df, window=20)
    plot_raw_vs_smoothed(df)

if __name__ == "__main__":
    main()