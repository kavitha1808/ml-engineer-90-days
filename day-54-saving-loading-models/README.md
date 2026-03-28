# Day 54 - Saving & Loading Models

## Objective
Learn how to save and load machine learning models using:

- Pickle
- Joblib

## Concepts Covered
- Model persistence
- Saving trained models
- Loading saved models
- Reusing models without retraining
- Saving preprocessing objects like scalers

## What This Project Does
- Loads the Iris dataset
- Splits into train and test sets
- Scales features using StandardScaler
- Trains a Logistic Regression model
- Saves model + scaler using:
  - Pickle
  - Joblib
- Loads them back
- Makes predictions again
- Confirms that performance remains the same after loading
- Saves classification report

## Files Created
- `models/model_pickle.pkl`
- `models/scaler_pickle.pkl`
- `models/model_joblib.pkl`
- `models/scaler_joblib.pkl`
- `outputs/classification_report.txt`

## Key Learning
- **Pickle** is useful for general Python object serialization
- **Joblib** is better for large NumPy arrays and scikit-learn models
- Always save:
  - trained model
  - preprocessing steps (scaler, encoder, etc.)

## Interview Point
Why save models?
- To deploy them later
- To avoid retraining every time
- To reuse in production pipelines
- To maintain consistency in predictions
