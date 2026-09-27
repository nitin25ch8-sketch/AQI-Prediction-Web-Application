# 🌍 AQI Prediction Web Application

A machine learning-based web application that predicts the **Air Quality Index (AQI)** using pollutant-specific AQI values. The project uses a **Random Forest Regression model**, **FastAPI** for the backend API, and **Streamlit** for the frontend.

---

## 📌 Project Overview

Air quality is an important environmental and public-health concern. This project uses machine learning to predict the overall AQI from individual pollutant AQI values.

The application accepts:

* CO AQI Value
* Ozone AQI Value
* NO₂ AQI Value
* PM2.5 AQI Value

and returns a predicted **AQI value** along with its corresponding AQI category.

### Application Architecture

```text
                    USER
                     │
                     ▼
             ┌───────────────┐
             │   Streamlit   │
             │   Frontend    │
             └───────┬───────┘
                     │
                  HTTP POST
                     │
                     ▼
             ┌───────────────┐
             │    FastAPI    │
             │    Backend    │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ Random Forest  │
             │     Model      │
             └───────┬───────┘
                     │
                     ▼
                Predicted AQI
                     │
                     ▼
             Streamlit Result
```

---

## ✨ Features

* 🌍 AQI prediction using Machine Learning
* 🤖 Random Forest Regression
* 🚀 FastAPI REST API
* 🎨 Streamlit web interface
* 📊 Pollutant-specific AQI inputs
* 📈 AQI category classification
* ⚡ Fast prediction
* 🔄 Frontend-backend API integration
* 📦 Saved ML model using Joblib
* 📖 Interactive FastAPI Swagger documentation

---

## 🧠 Machine Learning

### Dataset

The project uses the:

```text
AQI-and-Lat-Long-of-Countries.csv
```

The dataset contains AQI-related information including:

```text
AQI Value
CO AQI Value
Ozone AQI Value
NO2 AQI Value
PM2.5 AQI Value
Latitude
Longitude
```

### Features Used by the Model

The current prediction model uses:

| Feature         | Description                 |
| --------------- | --------------------------- |
| CO AQI Value    | Carbon monoxide AQI         |
| Ozone AQI Value | Ozone AQI                   |
| NO₂ AQI Value   | Nitrogen dioxide AQI        |
| PM2.5 AQI Value | Fine particulate matter AQI |

### Target

```text
AQI Value
```

### Model

The project uses:

```text
Random Forest Regressor
```

The trained model is saved as:

```text
aqi_random_forest_model.joblib
```

---

## 🛠️ Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Matplotlib
* Seaborn

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* Streamlit
* Python Requests

### Development

* Jupyter Notebook / Google Colab
* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
AQI-Prediction/
│
├── backend/
│   ├── main.py
│   ├── aqi_random_forest_model.joblib
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── notebooks/
│   └── AQI_Prediction.ipynb
│
├── data/
│   └── AQI-and-Lat-Long-of-Countries.csv
│
├── README.md
└── .gitignore
```

> **Note:** If your dataset or trained model is too large for GitHub, keep it out of the repository and provide instructions for obtaining/recreating it.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AQI-Prediction.git
```

Move into the project:

```bash
cd AQI-Prediction
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

### Backend

```bash
cd backend
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
fastapi
uvicorn
pydantic
joblib
pandas
scikit-learn
```

### Frontend

Open another terminal or return to the project directory:

```bash
cd frontend
pip install -r requirements.txt
```

Example:

```text
streamlit
requests
```

---

# ▶️ Running the Application

The backend and frontend need to run simultaneously.

## Step 1 — Start FastAPI

Open Terminal 1:

```bash
cd backend
```

Run:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### FastAPI documentation

Open:

```text
http://127.0.0.1:8000/docs
```

This opens the interactive Swagger API documentation.

---

## Step 2 — Start Streamlit

Open Terminal 2:

```bash
cd frontend
```

Run:

```bash
streamlit run app.py
```

The frontend will normally be available at:

```text
http://localhost:8501
```

---

# 🔌 API Documentation

## POST `/predict`

Predicts AQI based on pollutant AQI values.

### Request

```json
{
    "co_aqi_value": 10,
    "ozone_aqi_value": 20,
    "no2_aqi_value": 15,
    "pm2_5_aqi_value": 50
}
```

### Response

```json
{
    "predicted_aqi": 52.37
}
```

---

# 🔄 Prediction Workflow

```text
User enters pollutant values
            │
            ▼
       Streamlit UI
            │
            ▼
       JSON Request
            │
            ▼
       FastAPI /predict
            │
            ▼
    Random Forest Model
            │
            ▼
      AQI Prediction
            │
            ▼
       JSON Response
            │
            ▼
       Streamlit UI
            │
            ▼
     AQI + Category
```

---

# 📊 AQI Categories

The application displays an AQI category based on the predicted AQI.

|     AQI | Category                       |
| ------: | ------------------------------ |
|    0–50 | Good                           |
|  51–100 | Moderate                       |
| 101–150 | Unhealthy for Sensitive Groups |
| 151–200 | Unhealthy                      |
| 201–300 | Very Unhealthy                 |
|    301+ | Hazardous                      |

> **Important:** AQI category definitions depend on the AQI standard being used. If this project is presented as an India-specific application, the category system should be aligned with the applicable Indian AQI standard rather than automatically using the above U.S.-style ranges.

---

# 🧪 Machine Learning Workflow

The ML development process is:

```text
Dataset
   │
   ▼
Data Exploration
   │
   ▼
Data Cleaning
   │
   ▼
Feature Selection
   │
   ▼
Train/Test Split
   │
   ▼
Model Training
   │
   ├── Linear Regression
   ├── Decision Tree
   └── Random Forest
   │
   ▼
Model Evaluation
   │
   ├── MAE
   ├── MSE
   ├── RMSE
   └── R² Score
   │
   ▼
Random Forest
   │
   ▼
Save Model
   │
   ▼
aqi_random_forest_model.joblib
```

---

# 📈 Model Evaluation

The model can be evaluated using:

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted AQI.

### Mean Squared Error (MSE)

Penalizes larger prediction errors more heavily.

### Root Mean Squared Error (RMSE)

Provides an error measure in the same units as AQI.

### R² Score

Measures how well the model explains variation in the target variable.

Example:

```python
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = mse ** 0.5

r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)
```

---

# ⚠️ Important Dataset Consideration

The current dataset contains **pollutant-specific AQI values**, rather than raw pollutant concentrations.

For example:

```text
CO AQI Value
Ozone AQI Value
NO2 AQI Value
PM2.5 AQI Value
```

Therefore, this project predicts the overall `AQI Value` from pollutant-specific AQI values.

It is **not currently predicting AQI directly from raw measurements such as PM2.5 concentration in µg/m³, CO concentration, NO₂ concentration, etc.**

This distinction should be mentioned when presenting the project.

---

# 🔮 Future Improvements

Possible improvements include:

* [ ] Add raw pollutant concentration data
* [ ] Add PM10 concentration
* [ ] Add weather information
* [ ] Add temperature and humidity
* [ ] Add wind speed
* [ ] Add location-based AQI prediction
* [ ] Add interactive AQI charts
* [ ] Add historical prediction tracking
* [ ] Add database support
* [ ] Add user authentication
* [ ] Add model comparison dashboard
* [ ] Add model explainability
* [ ] Deploy the application online
* [ ] Add real-time air-quality data
* [ ] Add map-based AQI visualization

---

# 🔐 Environment & Security

For production deployment:

* Do not store API keys directly in source code.
* Use environment variables for secrets.
* Do not commit sensitive credentials.
* Use `.gitignore` for virtual environments and local configuration files.

Example `.gitignore`:

```text
venv/
__pycache__/
*.pyc
.env
.ipynb_checkpoints/
```

---

# 👨‍💻 Author

**Nitin Chauhan**

B.Tech Computer Science / Engineering Student

---

# 📜 License

This project is intended for **educational and academic purposes**.

You may modify and extend the project for learning and development purposes.
