# Day 49 - ML Pipelines (Preprocessing + Model Together)

## Objective
This project demonstrates how to combine **data preprocessing** and **machine learning model training** into a single workflow using **Scikit-learn Pipelines**.

Instead of manually preprocessing data and then training a model separately, we build a **pipeline** that performs:

- Missing value handling
- Feature scaling
- Categorical encoding
- Model training

all in one structured and reusable object.

---

## Concepts Covered

- ML Pipelines
- Preprocessing + Model Together
- `Pipeline`
- `ColumnTransformer`
- `SimpleImputer`
- `StandardScaler`
- `OneHotEncoder`
- `LogisticRegression`
- Train-Test Split
- Evaluation Metrics
- Confusion Matrix

---

## Why Pipelines Matter

In real-world machine learning, raw data usually contains:

- Missing values
- Numerical features that need scaling
- Categorical features that need encoding

If preprocessing is done manually, it can lead to:

- Data leakage
- Inconsistent transformations
- Messy code
- Harder deployment

Using a **Pipeline** solves this by ensuring that:

- The same preprocessing is applied during training and prediction
- Preprocessing happens only on training data when needed
- Code becomes cleaner and reusable

---

## Workflow

### 1. Create synthetic dataset
This project uses a small dataset containing:

- `age` (numerical)
- `salary` (numerical)
- `city` (categorical)
- `gender` (categorical)
- `bought` (target label)

It also intentionally includes missing values.

### 2. Split columns by type
- Numerical columns: `age`, `salary`
- Categorical columns: `city`, `gender`

### 3. Build preprocessing pipelines

#### Numerical pipeline:
- Fill missing values with mean
- Scale features using `StandardScaler`

#### Categorical pipeline:
- Fill missing values with most frequent value
- Apply `OneHotEncoder`

### 4. Combine preprocessing using `ColumnTransformer`

### 5. Build full pipeline
The final pipeline combines:

- Preprocessing
- Logistic Regression model

### 6. Train and predict
- `pipeline.fit(X_train, y_train)`
- `pipeline.predict(X_test)`

### 7. Evaluate model
- Accuracy
- Classification report
- Confusion matrix

---

## Output Files

### `raw_data_preview.png`
Preview of the dataset in table format.

### `target_distribution.png`
Bar chart showing how many samples belong to each target class.

### `missing_values_heatmap.png`
Simple visual showing where missing values are present in the dataset.

### `prediction_distribution.png`
Bar chart of predicted classes from the test set.

### `confusion_matrix.png`
Confusion matrix for model evaluation.


---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
