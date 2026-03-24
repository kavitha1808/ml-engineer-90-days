# Day 50 - End-to-End ML Workflow Revision

## Overview
This project is a revision of the complete end-to-end machine learning workflow using the Titanic dataset. It demonstrates how to move from raw data to a trained and saved model using preprocessing pipelines, evaluation metrics, and visual outputs.

## Objectives
- Load and inspect data
- Handle missing values
- Perform exploratory data analysis
- Build preprocessing pipelines
- Train a classification model
- Evaluate performance
- Save the trained model
- Make sample predictions

## Dataset
- Titanic dataset
- Target column: `Survived`

## Workflow Steps
1. Load dataset
2. Preview raw data
3. Visualize missing values
4. Analyze target distribution
5. Explore feature distribution
6. Select useful features
7. Build preprocessing pipeline
8. Split into train and test sets
9. Train Random Forest model
10. Predict on test data
11. Evaluate with accuracy, classification report, confusion matrix
12. Visualize feature importance
13. Save trained pipeline model
14. Run sample prediction

## Features Used
- `Pclass`
- `Sex`
- `Age`
- `Fare`
- `Embarked`

## Model Used
- Random Forest Classifier

## Libraries Used
- pandas
- matplotlib
- seaborn
- scikit-learn
- joblib

## Output Files
- `raw_data_preview.png`
- `missing_values_heatmap.png`
- `target_distribution.png`
- `age_distribution.png`
- `confusion_matrix.png`
- `feature_importance.png`


## Learning Outcomes
- Understood complete ML workflow from data loading to deployment-ready model saving
- Practiced preprocessing with `ColumnTransformer`
- Used `Pipeline` to avoid data leakage
- Evaluated model with multiple metrics
- Saved model for future reuse

## Run Command
```bash
python ml_workflow_revision.py
