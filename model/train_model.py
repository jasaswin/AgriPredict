"""
train_model.py
---------------
Step 1: Load dataset with Pandas
Step 2: Clean / preprocess
Step 3: Split into train/test
Step 4: Train a RandomForestClassifier
Step 5: Evaluate accuracy
Step 6: Save the trained model with joblib so Flask can load it later
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ---------- Step 1: Load dataset ----------
data = pd.read_csv("../data/crop_data.csv")
print("Dataset shape:", data.shape)
print(data.head())

# ---------- Step 2: Basic preprocessing ----------
# drop duplicate rows if any, drop rows with missing values
data = data.drop_duplicates()
data = data.dropna()

FEATURES = ["N", "P", "K", "temperature", "humidity", "rainfall", "ph"]
TARGET = "label"

X = data[FEATURES]
y = data[TARGET]

# ---------- Step 3: Train / test split ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---------- Step 4: Train model ----------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ---------- Step 5: Evaluate ----------
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\nTest accuracy: {acc * 100:.2f}%\n")
print(classification_report(y_test, y_pred))

# ---------- Step 6: Save model ----------
joblib.dump(model, "crop_model.pkl")
joblib.dump(FEATURES, "feature_order.pkl")
print("\nSaved trained model to model/crop_model.pkl")
