# Day 52 - Configuration Files + Parameter Management

This project demonstrates how configuration files and parameter management can be used to build a cleaner and more maintainable machine learning workflow.

## Objective
The goal of this project is to create a config-driven machine learning training pipeline using the Titanic dataset, where important settings are stored outside the main Python code.

## Features
- Loads configuration values from a YAML file
- Reads the Titanic dataset
- Drops unnecessary columns based on configuration
- Separates features and target column
- Encodes categorical variables using one-hot encoding
- Handles missing values using median imputation
- Splits data into training and testing sets
- Trains a Random Forest Classifier
- Saves the trained model file
- Saves evaluation metrics to a text file

## 📂 Project Structure
```bash
52-config-parameter-management/
│── data/
│   └── titanic.csv
│── configs/
│   └── config.yaml
│── models/
│── outputs/
│── src/
│   ├── config_loader.py
│   └── train.py
│── requirements.txt
│── README.md
```
## ▶️ How to Run

### 1. Install dependencies
```
pip install -r requirements.txt
```
### 2. Add dataset
Place titanic.csv inside the data/ folder.

### 3. Run the training script
```
python src/train.py
```


## Concepts Covered
- Configuration files
- YAML in machine learning projects
- Parameter management
- Clean and reusable ML code
- Model training workflow
- Output and artifact management

## Configuration Details
The configuration file stores:
- dataset path
- target column name
- columns to drop
- train-test split settings
- random seed
- model hyperparameters such as:
  - number of estimators
  - maximum depth
  - minimum samples split
- output paths for saved model and metrics

## Key Learning
Instead of hardcoding values inside Python scripts, configuration files allow important parameters to be managed separately. This makes the project easier to maintain, easier to modify for experiments, and more professional for real-world ML engineering workflows.

## Output
The project generates:
- a trained machine learning model file
- a metrics text file containing:
  - accuracy score
  - classification report

## Conclusion
This project shows how configuration-driven development improves machine learning projects by separating code logic from adjustable parameters. It is a foundational ML engineering practice that supports scalability, reusability, and better project organization.
