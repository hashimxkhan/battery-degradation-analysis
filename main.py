from src.load_data import load_battery_data
from src.plots import plot_raw_capacity

path = "data/battery_dataset.csv"

def main():
    df = load_battery_data(path)
    plot_raw_capacity(df)

if __name__ == "__main__":
    main()