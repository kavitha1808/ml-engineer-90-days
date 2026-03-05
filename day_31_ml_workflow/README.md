# Day 31 – Machine Learning Workflow (House Price Prediction)

## Overview

This project demonstrates a basic Machine Learning workflow using a house price dataset.

The model predicts house prices based on:

- House size (square feet)
- Number of bedrooms
- Age of the house

The project illustrates the standard ML pipeline:

Data Loading → Data Splitting → Model Training → Prediction → Evaluation

## Project Structure

day_31_ml_workflow/

data/
house_prices.csv

src/
train_model.py

outputs/
prediction_results.csv

README.md

## Dataset Description

The dataset contains the following columns:

size_sqft – House size in square feet  
bedrooms – Number of bedrooms  
house_age – Age of the house (years)  
price – Actual house price

## Technologies Used

Python  
Pandas  
Scikit-learn

## Machine Learning Workflow

1. Load the dataset
2. Define input features and target variable
3. Split the dataset into training and testing sets
4. Train a Linear Regression model
5. Make predictions on the test data
6. Evaluate the model using Mean Absolute Error
7. Save the predictions to a CSV file

## How to Run

Install required libraries:

pip install pandas scikit-learn

Run the script:

python src/train_model.py

## Output

The predicted results will be saved in:

outputs/prediction_results.csv
