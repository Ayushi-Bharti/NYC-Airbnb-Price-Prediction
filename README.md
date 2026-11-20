# NYC Airbnb Price Prediction

A Machine Learning project that predicts the estimated nightly price of Airbnb listings in New York City using listing details and geographical information.

## Project Overview

This project uses NYC Airbnb listing data to build a regression model that estimates the nightly price of a listing.

The trained model is integrated with a FastAPI REST API, allowing users to submit listing details and receive an estimated nightly price in USD.

## Features

- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Missing value handling
- Outlier filtering
- Categorical feature encoding
- Linear Regression and Random Forest model comparison
- Hyperparameter tuning using RandomizedSearchCV
- Model saving using Joblib
- REST API using FastAPI

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Jupyter Notebook

## Model Performance

The final Random Forest Regressor achieved the following results:

| Metric | Score |
|---|---:|
| MAE | $102.15 |
| RMSE | $181.25 |
| R² Score | 0.55 |

## Input Features

The model uses these seven features:

- Neighbourhood
- Room Type
- Latitude
- Longitude
- Accommodates
- Bedrooms
- Bathrooms

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/Ayushi-Bharti/NYC-Airbnb-Price-Prediction.git
```

**2. Navigate to the project folder**

```bash
cd NYC-Airbnb-Price-Prediction
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the environment (Windows)**

```bash
.venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Download the trained model**

Download `airbnb_price_pipeline.pkl` from the
[GitHub Releases](https://github.com/Ayushi-Bharti/NYC-Airbnb-Price-Prediction/releases/tag/v1.0.0).

Place the downloaded file in the project root directory.

**7. Run the API**

```bash
python -m uvicorn main:app --reload
```

## API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

**POST /predict**

Submit listing details in JSON format to receive the estimated nightly price in USD.

##  Future Improvements

- Integrate the prediction API with a full-stack Airbnb clone.
- Add INR currency conversion.
- Explore additional machine learning algorithms.
- Deploy the API to a cloud platform.

---

**Developed as a Machine Learning portfolio project.**
