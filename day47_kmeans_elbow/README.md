# Day 47 – K-Means Clustering and Elbow Method

## Overview
This project demonstrates **K-Means Clustering**, one of the most popular **unsupervised learning algorithms**, along with the **Elbow Method** used to determine the optimal number of clusters.

The project generates synthetic unlabeled data, scales it, applies K-Means clustering, visualizes clustered groups, and uses the Elbow Method to find the best value of **K**.

---

## Concepts Covered

- Unsupervised Learning
- Clustering
- K-Means Algorithm
- Cluster Centroids
- Within-Cluster Sum of Squares (WCSS)
- Inertia
- Elbow Method
- Feature Scaling using StandardScaler
- Cluster Visualization

---

## What This Project Does

- Creates a synthetic unlabeled dataset using `make_blobs`
- Visualizes the raw data
- Scales the data using `StandardScaler`
- Applies the **Elbow Method** for K values from 1 to 10
- Plots the Elbow graph using **WCSS / inertia**
- Selects the optimal number of clusters
- Trains a final **K-Means** model
- Predicts cluster labels for each data point
- Visualizes the clustered data
- Plots final cluster centroids

---

## K-Means Clustering – Explanation

K-Means is an **unsupervised machine learning algorithm** used to divide data into **K clusters** based on similarity.

### How it works:
1. Choose the number of clusters **K**
2. Randomly initialize **K centroids**
3. Assign each data point to the nearest centroid
4. Recalculate the centroids as the mean of assigned points
5. Repeat until centroids stop changing significantly

The algorithm tries to minimize the **Within-Cluster Sum of Squares (WCSS)**, also called **inertia**, which measures how close data points are to their assigned centroid.

---

## Elbow Method – Explanation

The **Elbow Method** is used to find the best number of clusters (**K**) for K-Means.

### Steps:
1. Run K-Means for different values of **K**
2. Record the **WCSS / inertia** for each K
3. Plot **K vs WCSS**
4. Find the point where the curve bends like an **elbow**

That elbow point represents the **optimal number of clusters**, where adding more clusters does not significantly improve clustering performance.

---

## Why Scaling is Important

K-Means uses **distance calculations** (usually Euclidean distance).  
If features have different scales, larger-scale features dominate the distance.

That is why the project uses:

- `StandardScaler`

This ensures all features contribute fairly to clustering.

---

## Outputs

### 1. `raw_unlabeled_data.png`
Scatter plot of the original synthetic unlabeled data.

### 2. `scaled_data.png`
Scatter plot of the scaled dataset after applying `StandardScaler`.

### 3. `kmeans_clustered_data.png`
Scatter plot showing the final clustered data points with different cluster colors.

### 4. `elbow_method.png`
Line plot of **K vs WCSS**, used to identify the optimal number of clusters.

### 5. `cluster_centroids.png`
Cluster visualization with data points colored by cluster and centroids marked clearly.

---

## Sample Console Output

- First 20 predicted cluster labels
- Final cluster centroid coordinates
- Final WCSS / inertia value

Example:
- Cluster Labels (first 20): [2 1 0 3 ...]
- Centroids: 4 cluster center coordinates
- Final Inertia: numerical WCSS value

---

## Libraries Used

- NumPy
- Matplotlib
- Scikit-learn

---

## Real-World Applications

- Customer segmentation
- Market analysis
- Student grouping based on performance
- Image compression
- Document clustering
- Product recommendation grouping
- Sales pattern segmentation
- Location hotspot analysis

---

## Key Learning Outcomes

By completing this project, you will understand:

- What clustering is in unsupervised learning
- How K-Means forms clusters
- Why centroids are important
- What WCSS / inertia means
- How to choose the best number of clusters using the Elbow Method
- Why feature scaling is essential before K-Means
- How to visualize clusters and centroids

