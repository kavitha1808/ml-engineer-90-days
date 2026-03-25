# Day 51 - Writing Modular ML Code

## Objective
Learn how to structure a machine learning project by separating logic into reusable modules such as data loading, preprocessing, training, and evaluation.

## Project Structure
```bash
51-modular-ml-code/
│── data/
│   └── titanic.csv
│
│── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│
│── main.py
│── requirements.txt
│── README.md
```
## Features
 - Loads Titanic dataset
 - Cleans missing values
 - Encodes categorical variables
 - Splits data into train and test sets
 - Trains a Random Forest Classifier
 - Evaluates model performance using accuracy, confusion matrix, and classification report

--- 

## Modules
  - data_loader.py → loads dataset
  - preprocess.py → handles cleaning and preprocessing
  - train.py → trains the model
  - evaluate.py → evaluates the model
  - main.py → runs the full ML pipeline

---

##  Requirements

Install dependencies:
```
pip install -r requirements.txt
```
## How to Run
python main.py
---

## Example Output
==================================================
Model Accuracy: 0.81
==================================================
Confusion Matrix:
[[90 15]
 [19 55]]
==================================================
Classification Report:
...
==================================================

---

##  Key Learning
  - Writing clean and modular ML code
  - Separating logic into dedicated files
  - Improving maintainability and reusability
  - Following a professional ML project structure

---
