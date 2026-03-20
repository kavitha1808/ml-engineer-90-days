import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# Create outputs folder
os.makedirs("outputs", exist_ok=True)


# -------------------------------
# 1. Generate synthetic data
# -------------------------------
X, y_true = make_blobs(
    n_samples=300,
    centers=3,
    cluster_std=1.2,
    random_state=42
)

# Save original raw data plot
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], s=40, edgecolor='k')
plt.title("Raw Unlabeled Data (Clustering Intuition)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/raw_unlabeled_data.png")
plt.close()


# -------------------------------
# 2. Feature scaling
# -------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save scaled data plot
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], s=40, edgecolor='k')
plt.title("Scaled Data")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/scaled_data.png")
plt.close()


# -------------------------------
# 3. Apply K-Means clustering
# -------------------------------
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)
centroids = kmeans.cluster_centers_

# Save clustered data plot
plt.figure(figsize=(8, 6))
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=cluster_labels,
    s=40,
    cmap="viridis",
    edgecolor='k'
)
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    s=250,
    marker='X',
    c='red',
    edgecolor='black',
    label='Centroids'
)
plt.title("K-Means Clustering Result")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/kmeans_clustered_data.png")
plt.close()


# -------------------------------
# 4. Elbow method (WCSS / Inertia)
# -------------------------------
inertias = []
k_values = range(1, 11)

for k in k_values:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(k_values, inertias, marker='o')
plt.title("Elbow Method (WCSS / Inertia)")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (WCSS)")
plt.xticks(k_values)
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/elbow_method.png")
plt.close()


# -------------------------------
# 5. Print useful output
# -------------------------------
print("Day 46 - Unsupervised Learning: Clustering Intuition")
print("=" * 55)
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Chosen number of clusters (K): {kmeans.n_clusters}")
print(f"K-Means Inertia (WCSS): {kmeans.inertia_:.4f}")
print("\nCluster Centers (scaled space):")
print(centroids)

unique, counts = np.unique(cluster_labels, return_counts=True)
print("\nCluster distribution:")
for label, count in zip(unique, counts):
    print(f"Cluster {label}: {count} points")

print("\nSaved output plots in 'outputs/' folder:")
print("- raw_unlabeled_data.png")
print("- scaled_data.png")
print("- kmeans_clustered_data.png")
print("- elbow_method.png")
