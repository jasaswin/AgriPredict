"""
generate_dataset.py
--------------------
Creates crop_data.csv used to train the AgriPredict model.

Each crop has a typical range for N, P, K, temperature, humidity,
rainfall and pH (based on general agronomy references). We sample
random values inside (and slightly around) those ranges to build a
synthetic but realistic dataset with several hundred rows.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

# crop: (N_range, P_range, K_range, temp_range, humidity_range, rainfall_range, ph_range)
CROPS = {
    "rice":       ((80, 120), (35, 60),  (35, 55),  (20, 32), (70, 95), (150, 300), (5.5, 7.0)),
    "maize":      ((60, 100), (35, 65),  (15, 40),  (18, 30), (50, 75), (60, 120),  (5.5, 7.5)),
    "chickpea":   ((10, 40),  (55, 85),  (75, 100), (15, 25), (14, 22), (60, 100),  (6.0, 8.0)),
    "cotton":     ((100, 140),(35, 65),  (15, 40),  (21, 35), (50, 80), (60, 110),  (5.8, 8.0)),
    "coffee":     ((80, 120), (15, 35),  (25, 45),  (18, 28), (50, 70), (150, 220), (6.0, 7.0)),
    "banana":     ((80, 120), (70, 100), (180, 220),(25, 35), (75, 90), (100, 180), (5.5, 6.8)),
    "mango":      ((10, 40),  (15, 40),  (25, 45),  (24, 35), (45, 60), (80, 150),  (5.5, 7.5)),
    "grapes":     ((10, 30),  (120, 150),(180, 210),(15, 30), (75, 90), (60, 100),  (5.8, 6.8)),
    "watermelon": ((80, 110), (10, 30),  (35, 55),  (24, 32), (55, 70), (40, 70),   (6.0, 7.0)),
    "muskmelon":  ((80, 110), (10, 30),  (35, 55),  (25, 32), (85, 95), (20, 30),   (6.0, 7.0)),
    "lentil":     ((15, 30),  (55, 80),  (18, 30),  (18, 30), (60, 70), (40, 60),   (6.0, 7.0)),
    "blackgram":  ((30, 55),  (55, 80),  (15, 25),  (25, 35), (60, 70), (60, 90),   (6.5, 7.5)),
    "mothbeans":  ((15, 30),  (35, 60),  (15, 25),  (24, 32), (40, 60), (30, 60),   (3.5, 9.9)),
    "mungbean":   ((15, 30),  (35, 60),  (15, 25),  (25, 35), (75, 90), (40, 65),   (6.2, 7.2)),
    "jute":       ((60, 100), (35, 55),  (35, 55),  (23, 30), (70, 90), (150, 200), (6.0, 7.5)),
    "coconut":    ((15, 35),  (10, 30),  (25, 40),  (25, 30), (90, 100),(120, 220), (5.2, 6.5)),
    "papaya":     ((30, 60),  (45, 70),  (45, 60),  (23, 35), (85, 95), (40, 120),  (6.0, 7.0)),
    "orange":     ((10, 30),  (5, 25),   (5, 15),   (10, 30), (85, 95), (100, 130), (6.0, 7.5)),
    "apple":      ((15, 35),  (120, 150),(190, 210),(15, 25), (85, 95), (100, 130), (5.5, 6.8)),
    "pomegranate":((15, 35),  (10, 30),  (35, 45),  (18, 30), (85, 95), (40, 110),  (5.5, 7.0)),
    "sugarcane":  ((90, 130), (35, 65),  (35, 65),  (24, 34), (65, 85), (150, 250), (6.0, 7.5)),
    "wheat":      ((40, 80),  (40, 70),  (30, 55),  (12, 25), (50, 65), (60, 100),  (6.0, 7.5)),
}

ROWS_PER_CROP = 60
records = []

for crop, (n_r, p_r, k_r, t_r, h_r, r_r, ph_r) in CROPS.items():
    for _ in range(ROWS_PER_CROP):
        n = np.random.uniform(*n_r)
        p = np.random.uniform(*p_r)
        k = np.random.uniform(*k_r)
        t = np.random.uniform(*t_r)
        h = np.random.uniform(*h_r)
        r = np.random.uniform(*r_r)
        ph = np.random.uniform(*ph_r)
        records.append([round(n, 1), round(p, 1), round(k, 1), round(t, 1),
                         round(h, 1), round(r, 1), round(ph, 2), crop])

df = pd.DataFrame(records, columns=["N", "P", "K", "temperature",
                                     "humidity", "rainfall", "ph", "label"])
df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # shuffle
df.to_csv("crop_data.csv", index=False)

print(f"Generated crop_data.csv with {len(df)} rows and {df['label'].nunique()} crops.")
