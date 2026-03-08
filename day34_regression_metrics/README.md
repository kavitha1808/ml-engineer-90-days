# Day 34 – Regression Evaluation Metrics

This project demonstrates how to evaluate regression models using common evaluation metrics.

Metrics used:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

Example problem: House Price Prediction

--------------------------------------------------

## Project Structure

day34_regression_metrics
│
├── regression_metrics.py
├── README.md
└── outputs
    └── error_visualization.png

--------------------------------------------------

## Concepts Covered

Regression models predict continuous numerical values such as house prices or sales revenue.

To measure model performance we use evaluation metrics.

### 1. Mean Absolute Error (MAE)

MAE calculates the average absolute difference between actual values and predicted values.

Formula:

MAE = (1/n) Σ |y − ŷ|

Advantages:
- Easy to interpret
- Same unit as target variable

Limitation:
- Does not penalize large errors strongly

--------------------------------------------------

### 2. Mean Squared Error (MSE)

MSE calculates the average squared difference between actual and predicted values.

Formula:

MSE = (1/n) Σ (y − ŷ)²

Advantages:
- Penalizes large errors strongly
- Useful for optimization algorithms

Limitation:
- Unit becomes squared which is harder to interpret

--------------------------------------------------

### 3. Root Mean Squared Error (RMSE)

RMSE is the square root of MSE and converts the error back to the original unit.

Formula:

RMSE = √MSE

Advantages:
- Easy interpretation
- Penalizes large errors

Limitation:
- Sensitive to outliers

--------------------------------------------------

## Example Dataset

Actual house prices

[200, 250, 300, 350, 400]

Predicted house prices

[210, 240, 310, 330, 390]

--------------------------------------------------

## Output

Example output:

MAE : 10.0  
MSE : 120.0  
RMSE : 10.95

--------------------------------------------------

## Visualization

The project also generates a plot comparing:

- Actual house prices
- Predicted house prices

Saved in:

outputs/error_visualization.png

--------------------------------------------------

## How to Run

1. Install required libraries

pip install numpy matplotlib scikit-learn

2. Run the script

python regression_metrics.py

--------------------------------------------------

## Applications

Regression evaluation metrics are widely used in:

- House price prediction
- Sales forecasting
- Weather prediction
- Stock price prediction
- Demand forecasting

