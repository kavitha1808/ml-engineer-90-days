# Day 30 – End-to-End ML Data Pipeline

## 📌 Project Overview

This project demonstrates a complete machine learning data pipeline:

Raw Data → Cleaning → Feature Engineering → Train/Test Split → Scaling → Model Training → Evaluation

The objective is to understand how raw data is transformed into ML-ready data using modular and reusable code.

---

## 📂 Folder Structure

day30-end-to-end-ml-pipeline/
│
├── data/
│   └── student_performance.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   └── evaluation.py
│
├── main.py
├── requirements.txt
└── README.md

---

## 🚀 Pipeline Steps

1. Load raw CSV data
2. Clean dataset (remove duplicates, handle missing values)
3. Perform feature engineering
4. Split into training and testing sets
5. Scale numerical features
6. Train Logistic Regression model
7. Evaluate model performance

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn

---

## ▶️ How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the pipeline:

python main.py

---

## 🎯 Learning Outcomes

- Understand end-to-end ML workflow
- Write modular and production-style code
- Convert raw data into ML-ready format
- Practice structured project organization

