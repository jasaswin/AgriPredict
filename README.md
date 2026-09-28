# 🌱 AgriPredict — Crop Recommendation System

AgriPredict is a crop recommendation system that predicts the most suitable
crop for a piece of farmland based on soil nutrients (N, P, K), temperature,
humidity, rainfall and soil pH.

The project uses a **Random Forest classifier** trained with scikit-learn,
served through a **Flask REST API**, with a simple **HTML, Bootstrap and
JavaScript frontend**.

🌐 **Live Demo:**  
https://agripredict-txr5.onrender.com

---

## 🚀 Live Application

You can try the deployed application here:

👉 **[AgriPredict — Live Demo](https://agripredict-txr5.onrender.com)**

The application is deployed on **Render** and includes both the frontend
and Flask backend in a single deployment.

---

## 📁 Project Structure

```text
AgriPredict/
├── data/
│   ├── generate_dataset.py   # Creates crop_data.csv (synthetic, 22 crops)
│   └── crop_data.csv         # Training dataset
│
├── model/
│   ├── train_model.py        # Trains & saves the Random Forest model
│   ├── crop_model.pkl        # Trained model
│   └── feature_order.pkl     # Feature column order
│
├── templates/
│   └── index.html            # Bootstrap + vanilla JavaScript frontend
│
├── app.py                    # Flask REST API and application entry point
├── requirements.txt          # Python dependencies
└── README.md

The trained model (crop_model.pkl) is already included in the repository,
so the application can be run immediately without retraining.

Retraining instructions are provided below if you want to regenerate the
model or use your own dataset.

✨ Features
🌱 Crop recommendation based on soil and weather conditions
🧪 Uses N, P, K soil nutrient values
🌡️ Temperature-based prediction
💧 Humidity and rainfall analysis
🧫 Soil pH consideration
🤖 Random Forest machine learning model
📊 Top-3 crop predictions with confidence percentages
⚡ Flask REST API
🎨 Responsive Bootstrap frontend
📱 Simple and user-friendly interface
🚀 Deployed online using Render
🛠️ Technologies Used
Backend
Python
Flask
NumPy
Pandas
Scikit-learn
Joblib
Gunicorn
Machine Learning
Random Forest Classifier
Train/Test Split
Synthetic crop recommendation dataset
Model serialization using Joblib
Frontend
HTML5
CSS3
Bootstrap
Vanilla JavaScript
Fetch API
Deployment
GitHub
Render
🚀 Quick Start
1. Clone the repository
git clone https://github.com/jasaswin/AgriPredict.git
cd AgriPredict
2. Install Python

Install Python 3.9+ if you don't already have it.

You can check your installed version with:

python --version
3. Install dependencies

Run:

pip install -r requirements.txt
4. Run the Flask application
python app.py

You should see the Flask application running locally.

5. Open the application

Open your browser and go to:

http://127.0.0.1:5000

Enter the soil and weather information and click Predict.

🔁 Optional — Retrain the Model

If you want to regenerate the dataset or retrain the model, follow these
steps.

Generate the dataset
cd data
python generate_dataset.py

This regenerates:

data/crop_data.csv
Train the model

Go back to the project root and enter the model directory:

cd ../model

Then run:

python train_model.py

This retrains the Random Forest model and generates:

model/crop_model.pkl

The feature order is stored in:

model/feature_order.pkl
🧠 How It Works
Farmer enters soil & weather information
                  ↓
             Flask App
                  ↓
          POST /predict API
                  ↓
       Feature Validation & Ordering
                  ↓
       Trained Random Forest Model
                  ↓
       Crop Prediction + Top-3
                  ↓
       Recommended Crop displayed
Prediction Process
The user enters soil and weather parameters.
The frontend sends the values to the Flask /predict endpoint.
Flask validates that all required features are present.
The input values are arranged in the exact order expected by the model.
The Random Forest model generates a crop prediction.
The model's prediction probabilities are calculated.
The top 3 probable crops are returned.
The frontend displays the recommended crop and confidence values.
🤖 Machine Learning Model

AgriPredict uses a:

RandomForestClassifier

The model is trained using the following features:

N
P
K
temperature
humidity
rainfall
ph

The target variable is:

label

The training process uses an 80/20 train-test split.

The trained model is saved using Joblib:

model/crop_model.pkl

This allows the Flask application to load the model directly without
retraining every time the application starts.

📊 Input Parameters

The application accepts the following parameters:

Parameter	Description
N	Nitrogen content in soil
P	Phosphorus content in soil
K	Potassium content in soil
temperature	Temperature
humidity	Humidity
rainfall	Rainfall
ph	Soil pH

Example:

N: 90
P: 42
K: 43
Temperature: 25.5
Humidity: 80
Rainfall: 200
pH: 6.5
📨 API Documentation
POST /predict

The /predict endpoint accepts soil and weather information as JSON and
returns the recommended crop along with the top 3 predictions.

Request
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 25.5,
  "humidity": 80,
  "rainfall": 200,
  "ph": 6.5
}
Response
{
  "recommended_crop": "rice",
  "top_3": [
    {
      "crop": "rice",
      "confidence": 82.0
    },
    {
      "crop": "jute",
      "confidence": 9.0
    },
    {
      "crop": "sugarcane",
      "confidence": 4.0
    }
  ]
}
🧪 Testing the API

You can test the API using Postman or curl.

Local API
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"N\":90,\"P\":42,\"K\":43,\"temperature\":25.5,\"humidity\":80,\"rainfall\":200,\"ph\":6.5}"
Live API

The deployed API is available at:

https://agripredict-txr5.onrender.com/predict

Example:

curl -X POST https://agripredict-txr5.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d "{\"N\":90,\"P\":42,\"K\":43,\"temperature\":25.5,\"humidity\":80,\"rainfall\":200,\"ph\":6.5}"
🌐 Deployment

AgriPredict is deployed using Render.

Deployment Architecture
                    GitHub
                       │
                       ↓
              Render Deployment
                       │
                       ↓
              Flask Application
                 /           \
                ↓             ↓
          HTML Frontend    ML Model
                              │
                              ↓
                       Crop Prediction

Since the frontend is served directly through Flask using:

@app.route("/")
def home():
    return render_template("index.html")

both the frontend and backend are deployed together on Render.

Live URL

👉 https://agripredict-txr5.onrender.com

Notes
The dataset in data/crop_data.csv is synthetically generated from
typical agronomic ranges for 22 crops.
The project is designed as a machine learning demonstration project.
The trained model is already included in the repository.
The model can be replaced with a real-world crop recommendation dataset.
If using a different dataset, maintain the required feature columns:
N
P
K
temperature
humidity
rainfall
ph
label
Predictions are dependent on the data used to train the model.
Inputs outside the ranges represented in the training dataset may produce
less meaningful recommendations.


