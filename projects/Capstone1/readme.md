# New York Traffic Accident Predictor

## Problem Description
Traffic accidents are a significant concern in New York, impacting public safety and causing economic losses. This project aims to predict the severity of traffic accidents using various features such as weather conditions, road conditions, and vehicle types. By accurately predicting accident severity, city planners and emergency services can better allocate resources and implement preventive measures.

## Dataset
- **Source**: [Kaggle - Traffic Accidents in NY 2023](https://www.kaggle.com/datasets/hfan83/traffic-accidents-in-ny-2023/data)
- **Features**: AccidentID, DateTime, County, WeatherCondition, RoadCondition, VehicleType, SeverityLevel, NumberOfVehicles, NumberOfInjuries, Cause, Junction, Traffic_Signal, Bump
- **Target Variable**: SeverityLevel

### Getting the Data

bash
wget https://www.kaggle.com/datasets/hfan83/traffic-accidents-in-ny-2023/data -O data/traffic_accidents_in_NY.csv

## Project Structure

├── README.md # Project documentation
├── notebook.ipynb # Jupyter notebook with EDA and model development
├── train.py # Script for training the final model
├── predict.py # Script for serving predictions
├── data/ # Data directory
├── models/ # Saved model files
├── Dockerfile # Dockerfile for containerization
└── requirements.txt # Project dependencies

## Environment Setup

### Local Development

bash
Create virtual environment
python -m venv venv
Activate virtual environment
On Windows:
venv\Scripts\activate
On Unix or MacOS:
source venv/bin/activate
Install dependencies
pip install -r requirements.txt

### Using Docker

bash
Build the Docker image
docker build -t ny-traffic-predictor .
Run the container
docker run -p 5000:5000 ny-traffic-predictor


## Model Development

### Exploratory Data Analysis
- Data cleaning and preparation
- Feature analysis and importance
- Target variable distribution

### Model Training
- Models evaluated: Random Forest, XGBoost, Neural Network
- Hyperparameter tuning using Optuna
- Final model: Random Forest with best parameters

## Running the Project

### Training the Model

bash
python train.py


### Making Predictions

bash
python predict.py


## API Documentation

### Prediction Endpoint

bash
curl -X POST -H "Content-Type: application/json" \
-d '{"County": "Queens", "WeatherCondition": "Rainy", "RoadCondition": "Dry", "VehicleType": "Car", "Cause": "Drunk Driving", "Junction": false, "Traffic_Signal": true, "Bump": false}' \
http://localhost:5000/predict



