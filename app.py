"""
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

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and the feature order it expects
model = joblib.load("model/crop_model.pkl")
FEATURES = joblib.load("model/feature_order.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()

        # Basic validation: make sure every required field is present
        missing = [f for f in FEATURES if f not in input_data]
        if missing:
            return jsonify({"error": f"Missing fields: {missing}"}), 400

        # Build the feature array in the exact order the model was trained on
        values = [float(input_data[f]) for f in FEATURES]
        X = np.array(values).reshape(1, -1)

        prediction = model.predict(X)[0]

        # Also return top-3 probable crops so the UI can show extra info
        probabilities = model.predict_proba(X)[0]
        classes = model.classes_
        top3_idx = np.argsort(probabilities)[::-1][:3]
        top3 = [
            {"crop": classes[i], "confidence": round(float(probabilities[i]) * 100, 2)}
            for i in top3_idx
        ]

        return jsonify({
            "recommended_crop": prediction,
            "top_3": top3
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
