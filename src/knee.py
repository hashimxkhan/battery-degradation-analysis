import pandas as pd
import numpy as np

def detect_knee(df: pd.DataFrame, baseline_window: int = 40, post_window: int = 5,slope_ratio_threshold: float = 1.5):

    results = []
    for battery_id, g in df.groupby("battery_id"):
        g = g.sort_values("cycle").reset_index(drop=True)

        # STEP 1: confirmation point
        accel_idx = g.index[g["persistent_accel"] == True]

        if len(accel_idx) == 0:
            results.append({
                "battery_id": battery_id,
                "knee_cycle": None,
                "confidence": 0.0
            })
            continue

        confirm_idx = accel_idx[0]

        # STEP 2: regime comparison
        baseline_start = max(0, confirm_idx - baseline_window)
        baseline_slope = g.loc[
            baseline_start:confirm_idx, "rolling_slope"
        ].mean()

        post_end = min(len(g), confirm_idx + post_window)
        post_slope = g.loc[
            confirm_idx:post_end, "rolling_slope"
        ].mean()

        if abs(post_slope) < abs(baseline_slope) * slope_ratio_threshold:
            results.append({
                "battery_id": battery_id,
                "knee_cycle": None,
                "confidence": 0.0
            })
            

        # STEP 3: backtrack to knee onset
        target_slope = post_slope

        knee_idx = confirm_idx
        for i in range(confirm_idx, -1, -1):
            if abs(g.loc[i, "rolling_slope"]) < abs(target_slope) * 0.9:
                knee_idx = i + 1
                break

        knee_cycle = g.loc[knee_idx, "cycle"]


        # STEP 4: confidence score
        slope_change = abs(post_slope / baseline_slope)
        persistence_len = len(accel_idx)

        confidence = min(
            1.0,
            0.5 * min(slope_change / 2.0, 1.0) +
            0.5 * min(persistence_len / 20.0, 1.0)
        )

        results.append({
            "battery_id": battery_id,
            "knee_cycle": int(knee_cycle),
            "confidence": round(confidence, 2)
        })

    return pd.DataFrame(results)