# 🌱 AgriPredict — Crop Recommendation System

AgriPredict predicts the most suitable crop for a piece of farmland based on
soil nutrients (N, P, K), temperature, humidity, rainfall and soil pH, using
a Random Forest classifier trained with scikit-learn, served through a
Flask REST API, with a simple HTML/Bootstrap/JavaScript frontend.

## 📁 Project structure

```
AgriPredict/
├── data/
│   ├── generate_dataset.py   # creates crop_data.csv (synthetic, 22 crops)
│   └── crop_data.csv         # training dataset
├── model/
│   ├── train_model.py        # trains & saves the RandomForest model
│   ├── crop_model.pkl        # trained model (already included)
│   └── feature_order.pkl     # feature column order (already included)
├── templates/
│   └── index.html            # Bootstrap + vanilla JS frontend
├── app.py                    # Flask REST API
├── requirements.txt
└── README.md
```

The trained model (`crop_model.pkl`) is already included, so you can run the
app immediately without retraining. Retraining steps are included below if
you want to regenerate it or use your own dataset.

## 🚀 Quick start

1. **Install Python 3.9+** if you don't already have it.

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**

   ```bash
   python app.py
   ```

4. **Open the app**

   Go to `http://127.0.0.1:5000` in your browser. Fill in the form and click
   **Predict**.

## 🔁 (Optional) Retrain the model

If you want to regenerate the dataset or retrain the model:

```bash
cd data
python generate_dataset.py      # regenerates crop_data.csv

cd ../model
python train_model.py           # retrains and overwrites crop_model.pkl
```

You can also swap `data/crop_data.csv` for a real-world dataset (for
example, the popular "Crop Recommendation Dataset" on Kaggle) as long as it
has the same columns: `N, P, K, temperature, humidity, rainfall, ph, label`.

## 🧠 How it works

```
Farmer enters soil & weather information
              ↓
        Flask REST API  (POST /predict)
              ↓
        Data preprocessing (feature ordering)
              ↓
       Trained Random Forest Model
              ↓
        Crop Prediction (+ top-3 confidences)
              ↓
       Recommended Crop shown on the page
```

- **Pandas** loads and cleans `crop_data.csv` (drops duplicates/missing
  values) in `train_model.py`.
- **scikit-learn**'s `train_test_split` splits the data 80/20 into
  train/test sets.
- A **RandomForestClassifier** (100 trees) is trained on the training set
  and evaluated on the test set (~97% accuracy on this synthetic dataset).
- **joblib** saves the trained model to `model/crop_model.pkl` so Flask can
  load it instantly without retraining.
- **Flask** exposes a single `POST /predict` endpoint that accepts JSON,
  runs it through the model, and returns the recommended crop plus the
  top-3 most likely crops with confidence percentages.
- The **frontend** (`templates/index.html`) is plain Bootstrap + vanilla
  JavaScript — no build tools, no frameworks — that calls `/predict` with
  `fetch()` and displays the result.

## 📨 API example

**Request** — `POST /predict`

```json
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 25.5,
  "humidity": 80,
  "rainfall": 200,
  "ph": 6.5
}
```

**Response**

```json
{
  "recommended_crop": "rice",
  "top_3": [
    { "crop": "rice", "confidence": 82.0 },
    { "crop": "jute", "confidence": 9.0 },
    { "crop": "sugarcane", "confidence": 4.0 }
  ]
}
```

You can test this endpoint directly with Postman or `curl`:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"N":90,"P":42,"K":43,"temperature":25.5,"humidity":80,"rainfall":200,"ph":6.5}'
```

## 📝 Notes

- The dataset in `data/crop_data.csv` is **synthetically generated** from
  typical agronomic ranges for 22 crops (see `generate_dataset.py`) so the
  project works fully offline. Swap in a real dataset for production use.
-"""
app.py
------
Simple Flask REST API for AgriPredict.

Routes:
    GET  /              -> serves the frontend (index.html)
    POST /predict        -> takes soil/weather values as JSON, returns predicted crop

Run with:
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""


