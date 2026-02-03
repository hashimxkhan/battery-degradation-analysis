import matplotlib.pyplot as plt

def plot_raw_capacity(df):
    for battery_id, group in df.groupby("battery_id"):
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

def plot_raw_vs_smoothed(df):
    for battery_id, group in df.groupby("battery_id"):
        plt.figure()
        plt.plot(group["cycle"], group["norm_capacity"], label="Raw")
        plt.plot(group["cycle"], group["smooth_capacity"], label="Smoothed")
        plt.xlabel("Cycle")
        plt.ylabel("Normalized Capacity")
        plt.title(f"Battery {battery_id}: Raw vs Smoothed Capacity")
        plt.legend()
        plt.tight_layout()
        plt.show()

def plot_rolling_slope(df):
    for battery_id, group in df.groupby("battery_id"):
        plt.figure()

        plt.plot(
            group["cycle"],
            group["rolling_slope"],
            label="Rolling slope"
        )

        plt.axhline(0, linestyle="--", color="gray", linewidth=1)
        plt.xlabel("Cycle")
        plt.ylabel("Rolling Slope (ΔCapacity per Cycle)")
        plt.title(f"Battery {battery_id}: Degradation Rate Over Time")
        plt.legend()
        plt.tight_layout()
        plt.show()