# 📊 Day 20 – Data Cleaning with Pandas

## 📌 Overview

This repository contains mini projects focused on **real-world data cleaning techniques using Pandas**.  
The goal of this day was to understand how to handle dirty datasets before applying Machine Learning models.

Data preprocessing is one of the most important stages in the ML pipeline, as real-world datasets often contain missing values, duplicates, inconsistent formats, and incorrect data types.

---

## 🧠 Concepts Covered

- Identifying missing values (`isnull`, `sum`)
- Dropping missing data (`dropna`)
- Filling missing values (Mean, Median, Mode, Constants)
- Removing duplicate rows
- Cleaning string columns (`strip`)
- Fixing data types (`astype`)
- Creating new calculated columns
- Preparing clean datasets for analysis

---

## 📁 Project Structure

day20_Data_Cleaning_and_ML/
   ├── employee_data_cleaner.py
   ├── sales_data_cleaner.py
   ├── hospital_data_cleaner.py
   └── README.md

---

# 🧾 Projects Included

---

## 1️⃣ Employee Data Cleaner

### 🎯 Objective
Clean employee dataset by:
- Handling missing Age, Salary, Experience
- Removing duplicate records
- Fixing department text formatting
- Correcting data types

### 🛠 Techniques Used
- Mean & median imputation
- Mode replacement
- Duplicate removal
- String cleaning
- Data type conversion

### ✅ Outcome
Structured and clean employee dataset ready for analytics or ML.

---

## 2️⃣ Sales Data Cleaner

### 🎯 Objective
Clean sales dataset and compute accurate revenue.

### 🛠 Techniques Used
- Filling missing prices using median
- Replacing missing quantities with default values
- Removing duplicates
- Creating a new feature: `Revenue = Price × Quantity`

### ✅ Outcome
Cleaned sales dataset with accurate total revenue calculation.

---

## 3️⃣ Hospital Data Cleaner

### 🎯 Objective
Prepare hospital patient data for machine learning usage.

### 🛠 Techniques Used
- Median imputation for Age
- Mean imputation for Blood Pressure & Cholesterol
- Filling categorical missing values
- Converting categorical target ("Yes"/"No") into numeric format (1/0)

### ✅ Outcome
Fully cleaned and ML-ready healthcare dataset.

---

# 🧰 Technologies Used

- Python
- Pandas
- NumPy

---

# 🚀 Key Learning Outcomes

After completing this module, I can:

- Handle missing data using multiple strategies
- Decide when to drop vs fill missing values
- Clean and standardize real-world datasets
- Perform feature correction and transformation
- Prepare structured datasets for further ML processing

---

# 📌 Why This Matters

Data cleaning typically consumes **70–80% of a data scientist’s time**.  
Mastering preprocessing ensures better model accuracy and reliable analysis.

---
  
