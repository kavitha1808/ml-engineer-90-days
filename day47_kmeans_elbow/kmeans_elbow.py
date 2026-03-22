import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# -----------------------------
# Create output folder
# -----------------------------
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# 1. Generate synthetic unlabeled data
# -----------------------------
X, _ = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=1.2,
    random_state=42
)

# -----------------------------
# 2. Plot raw unlabeled data
# -----------------------------
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], alpha=0.7)
plt.title("Raw Unlabeled Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/raw_unlabeled_data.png")
plt.show()

# -----------------------------
# 3. Scale the data
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# 4. Plot scaled data
# -----------------------------
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], alpha=0.7)
plt.title("Scaled Data")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/scaled_data.png")
plt.show()

# -----------------------------
# 5. Elbow Method to find optimal K
# -----------------------------
wcss = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot elbow method
plt.figure(figsize=(8, 6))
plt.plot(k_values, wcss, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS / Inertia")
plt.xticks(k_values)
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/elbow_method.png")
plt.show()

# -----------------------------
# 6. Train final K-Means model
# -----------------------------
optimal_k = 4
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
cluster_labels = kmeans_final.fit_predict(X_scaled)
centroids = kmeans_final.cluster_centers_

print("Cluster Labels (first 20):", cluster_labels[:20])
print("Centroids:\n", centroids)
print("Final Inertia (WCSS):", kmeans_final.inertia_)

# -----------------------------
# 7. Plot clustered data
# -----------------------------
plt.figure(figsize=(8, 6))
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=cluster_labels,
    cmap='viridis',
    alpha=0.7
)
plt.title("K-Means Clustered Data")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/kmeans_clustered_data.png")
plt.show()

# -----------------------------
# 8. Plot clustered data with centroids
# -----------------------------
plt.figure(figsize=(8, 6))
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=cluster_labels,
    cmap='viridis',
    alpha=0.7,
    label="Data Points"
)
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    s=300,
    marker='X',
    c='red',
    edgecolors='black',
    label='Centroids'
)
plt.title("K-Means Clusters with Centroids")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/cluster_centroids.png")
plt.show()
