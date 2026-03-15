# Day 41 - Decision Trees Theory and Splitting Criteria

## 📌 Objective
This project demonstrates the **Decision Tree Classifier** algorithm and explains how it uses **splitting criteria** such as **Gini Impurity** and **Entropy (Information Gain)** to make decisions.

---

## 📚 Theory

### What is a Decision Tree?
A **Decision Tree** is a supervised machine learning algorithm used for **classification** and **regression** tasks.

It works like a flowchart:
- The **root node** represents the starting feature.
- **Internal nodes** represent decisions based on feature values.
- **Branches** represent outcomes of those decisions.
- **Leaf nodes** represent final predictions.

Decision Trees are easy to understand and visualize.

---

## 🌳 How Decision Trees Work
1. Start with the full dataset.
2. Select the **best feature** to split the data.
3. Split the data into smaller groups.
4. Repeat the process recursively.
5. Stop when:
   - all samples belong to one class,
   - maximum depth is reached,
   - or no better split is possible.

---

## ✂️ Splitting Criteria

Decision Trees decide the **best split** using impurity measures.

### 1. Gini Impurity
Gini Impurity measures how often a randomly chosen element would be incorrectly classified.

**Formula:**

Gini = 1 - Σ(pᵢ²)

Where:
- pᵢ = probability of class i

**Interpretation:**
- Lower Gini = better split
- Gini = 0 means pure node

---

### 2. Entropy
Entropy measures the randomness or disorder in the data.

**Formula:**

Entropy = - Σ(pᵢ log₂ pᵢ)

**Interpretation:**
- Lower Entropy = purer node
- Entropy = 0 means pure node

---

### 3. Information Gain
Information Gain tells us how much entropy is reduced after a split.

**Formula:**

Information Gain = Entropy(parent) - Weighted Entropy(children)

**Interpretation:**
- Higher Information Gain = better split

---

## ⚖️ Gini vs Entropy

| Criteria | Gini Impurity | Entropy |
|----------|---------------|---------|
| Speed | Faster | Slightly slower |
| Formula | Simpler | More complex |
| Use Case | Default in many libraries | Useful when information theory interpretation is needed |
| Output | Similar results in many cases | Similar results in many cases |

---

## 🧪 Dataset Used
- **Iris Dataset**
- 3 flower classes:
  - Setosa
  - Versicolor
  - Virginica

---

## 🛠️ What This Project Does
- Loads the Iris dataset
- Splits data into train and test sets
- Trains a **Decision Tree Classifier**
- Uses **Gini criterion**
- Evaluates model performance
- Visualizes the decision tree
- Plots feature importance
- Compares **Gini vs Entropy**

---

## ▶️ How to Run

```bash
pip install numpy matplotlib scikit-learn
python decision_tree_theory.py
