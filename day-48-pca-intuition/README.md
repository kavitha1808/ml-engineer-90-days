# Day 48 – Dimensionality Reduction & PCA Intuition

## Overview
This project demonstrates the intuition behind **Dimensionality Reduction** using **Principal Component Analysis (PCA)**.

PCA is a feature extraction technique that reduces the number of dimensions in a dataset while preserving as much important information (variance) as possible.

This project includes:
- A **simple 2D synthetic dataset** with correlated features
- PCA projection from **2D to 1D**
- A visualization of **explained variance**
- PCA applied to the **Iris dataset** to reduce 4 features into 2 principal components

---

## Concepts Covered
- Dimensionality reduction
- Feature extraction
- PCA intuition
- Correlated features
- Principal components
- Explained variance ratio
- Cumulative explained variance
- 2D visualization of high-dimensional data

---

# **Project Structure**

```bash
day-48-pca-intuition/
│── main.py
│── README.md
│── outputs/
│   ├── original_2d_data.png
│   ├── pca_projection_2d.png
│   ├── explained_variance.png
│   └── pca_iris_2d_visualization.png
```
---

## What This Project Does

### 1. Synthetic 2D Correlated Data
A simple dataset with 2 correlated features is created.

This helps visualize:
- Why dimensionality reduction is useful
- How PCA finds the direction of maximum variance
- How data can be projected onto a lower dimension

---

### 2. PCA Projection (2D → 1D)
The 2D data is standardized and reduced into **1 principal component**.

Then it is reconstructed back to 2D for visualization to show:
- The original data distribution
- The PCA-compressed representation along the main direction

---

### 3. Explained Variance on Iris Dataset
PCA is applied to the full Iris dataset to calculate:
- How much variance each principal component captures
- How much total information is retained cumulatively

This helps decide:
- How many principal components should be kept

---

### 4. Iris Dataset PCA Visualization (4D → 2D)
The original Iris dataset has 4 features:
- sepal length
- sepal width
- petal length
- petal width

PCA reduces it to 2 principal components so that it can be visualized in a 2D plot.

This helps show:
- Class separation after dimensionality reduction
- Real-world use of PCA for visualization

---

## Key PCA Intuition
PCA works by finding new axes called **Principal Components**:

- **PC1** = direction of maximum variance
- **PC2** = second highest variance, orthogonal to PC1
- and so on...

Instead of keeping all original features, PCA keeps the most informative directions.

---

## Why Standardization is Important
Before applying PCA, the data is standardized using `StandardScaler`.

This is important because:
- Features may have different scales
- PCA is variance-based
- Large-scale features can dominate the result if scaling is skipped

---

## Output Files

```bash
outputs/
├── original_2d_data.png
├── pca_projection_2d.png
├── explained_variance.png
└── pca_iris_2d_visualization.png
