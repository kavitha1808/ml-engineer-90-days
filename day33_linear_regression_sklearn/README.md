# Day 33 – Linear Regression with Scikit-Learn

## Overview
This project demonstrates how to implement **Linear Regression using Scikit-learn** and evaluate the model using a **Train-Test Split**.  
The goal of the project is to predict **sales revenue based on marketing budget**.

---

## Problem Statement
Businesses invest money in marketing campaigns and want to estimate how much revenue those campaigns will generate.  
This project builds a machine learning model that learns the relationship between **marketing budget** and **sales revenue**.

---

## Dataset

File: `marketing_sales.csv`

Columns:

marketing_budget – Amount spent on marketing  
sales – Revenue generated

Example Data:

marketing_budget,sales  
5000,55000  
7000,65000  
8000,72000  
4000,50000  
10000,90000  

---

## Project Structure
day33_linear_regression_sklearn

│
├── data
│   └── marketing_sales.csv
│
├── src
│   └── train_model.py
│
├── outputs
│   └── regression_plot.png
│
└── README.md

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## Machine Learning Workflow

1. Load dataset
2. Define feature and target variables
3. Split dataset into training and testing data
4. Train Linear Regression model
5. Make predictions
6. Evaluate model performance
7. Visualize regression results

---

## Train-Test Split

The dataset is divided into:

80% Training Data  
20% Testing Data

Training data is used to train the model, while testing data is used to evaluate how well the model performs on unseen data.

---

## Model Used

Linear Regression

Linear Regression models the relationship between variables using a straight line.

Formula:

y = mx + b

Where:

y = predicted value  
m = slope  
x = input variable  
b = intercept

---

## Model Evaluation

Two metrics are used:

Mean Squared Error (MSE)  
Measures the average squared difference between predicted and actual values.

R² Score  
Measures how well the model explains the variance in the data.

Range:

0 → Poor model  
1 → Perfect model

---

## Output

The model generates a visualization showing the regression line.

outputs/regression_plot.png

The plot shows:
- Data points representing actual values
- Regression line representing predicted relationship

---

## How to Run the Project

Install dependencies:

pip install pandas matplotlib scikit-learn

Run the script:

python src/train_model.py

The script will train the model and save the regression plot.

---

## Real World Applications

- Marketing analytics
- Sales forecasting
- Business revenue prediction
- Financial analysis
- Real estate price prediction
