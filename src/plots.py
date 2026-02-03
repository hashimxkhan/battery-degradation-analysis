import matplotlib.pyplot as plt

def plot_raw_capacity(df):
    for battery_id, group in df.groupby("battery_id"):
        if battery_id in  ["B6", "B7"]:
            plt.plot(
            group["cycle"],
            group["BCt"],
            label=battery_id
            )

    plt.xlabel("Cycle")
    plt.ylabel("Battery Capacity (BCt)")
    plt.title("Battery Capacity vs Cycle #")
    plt.legend()
    plt.tight_layout()
    plt.show()