# Battery Degradation Analysis

This project is a practical battery degradation analysis pipeline built step by step to detect the knee point, where capacity fade begins to accelerate.

The workflow starts from raw cycle data, applies preprocessing and feature engineering, and ends with binary knee detection plus a confidence score per battery.

## What I built in this project

The project was developed in clear stages:

- `v0`: tested raw data progression and basic plotting.
- `v1`: added preprocessing (capacity normalization and smoothing).
- `v2`: added degradation-rate features (rolling slope and curvature) and persistence logic.
- `v3`: added binary knee detection with regime comparison, backtracking, and confidence scoring.

## Current pipeline

For each battery:

1. Load and validate required columns (`battery_id`, `cycle`, `BCt`).
2. Normalize capacity using each battery's first observed capacity.
3. Smooth normalized capacity with a rolling mean.
4. Compute rolling slope (degradation rate).
5. Compute curvature (change in slope) after an initial minimum cycle region.
6. Detect persistent acceleration using a threshold + persistence window.
7. Detect knee cycle using:
   - first persistent acceleration as a confirmation point,
   - baseline vs post-confirmation slope ratio check,
   - backtracking to find the knee onset,
   - confidence score from slope change and persistence strength.

## Repository structure

- `main.py` - Orchestrates the full analysis pipeline.
- `src/load_data.py` - CSV loading and input validation.
- `src/preprocess.py` - Normalization and smoothing.
- `src/features.py` - Rolling slope, curvature, and persistence features.
- `src/knee.py` - Knee detection and confidence scoring.
- `src/plots.py` - Visualizations for each stage.
- `data/Battery_dataset.csv` - Input dataset.
- `requirements.txt` - Python dependencies.

## How to run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the project

```bash
python main.py
```

## What to expect when running

- Several matplotlib plots open in sequence:
  - raw capacity vs cycle,
  - raw vs smoothed normalized capacity,
  - rolling slope over cycles,
  - curvature with persistent-acceleration points highlighted.
- Console output includes:
  - rolling slope table,
  - curvature + persistence table,
  - final knee detection table with `battery_id`, `knee_cycle`, and `confidence`.

## Notes

- The script currently uses a relative dataset path inside `main.py`.
- The pipeline is battery-wise and uses grouped rolling operations.
- Knee detection can return `None` when acceleration evidence is not strong enough.

## Future work

- Add CLI arguments for data path and hyperparameters (`window`, thresholds, persistence).
- Save plots and output tables to files instead of only showing/printing.
- Add unit tests for each pipeline stage.
- Add experiment tracking for threshold tuning.
- Compare this heuristic method with piecewise regression / changepoint models.
- Make path handling cross-platform and case-safe.

## Tech stack

- Python
- pandas
- numpy
- matplotlib
