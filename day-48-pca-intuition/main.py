import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# Create outputs folder
os.makedirs("outputs", exist_ok=True)


# =========================================================
# 1. PCA on simple 2D synthetic data
# =========================================================
np.random.seed(42)

# Generate correlated 2D data
mean = [0, 0]
cov = [[3, 2.5], [2.5, 3]]  # correlated features
X_2d = np.random.multivariate_normal(mean, cov, 300)

# Plot original 2D data
plt.figure(figsize=(8, 6))
plt.scatter(X_2d[:, 0], X_2d[:, 1], alpha=0.7)
plt.title("Original 2D Correlated Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/original_2d_data.png")
plt.close()

# Standardize data
scaler_2d = StandardScaler()
X_2d_scaled = scaler_2d.fit_transform(X_2d)

# Apply PCA to reduce 2D -> 1D
pca_2d = PCA(n_components=1)
X_2d_pca = pca_2d.fit_transform(X_2d_scaled)

# Reconstruct back to 2D for visualization
X_2d_reconstructed = pca_2d.inverse_transform(X_2d_pca)

# Plot original and PCA projection
plt.figure(figsize=(8, 6))
plt.scatter(X_2d_scaled[:, 0], X_2d_scaled[:, 1], alpha=0.4, label="Original (scaled)")
plt.scatter(
    X_2d_reconstructed[:, 0],
    X_2d_reconstructed[:, 1],
    alpha=0.8,
    label="Projected onto PC1"
)
plt.title("PCA Projection (2D → 1D → Reconstructed)")
plt.xlabel("Scaled Feature 1")
plt.ylabel("Scaled Feature 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/pca_projection_2d.png")
plt.close()


# =========================================================
# 2. Explained variance on Iris dataset
# =========================================================
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Standardize iris features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA with all components
pca_full = PCA()
X_pca_full = pca_full.fit_transform(X_scaled)

explained_variance = pca_full.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

# Plot explained variance
plt.figure(figsize=(8, 6))
plt.bar(
    range(1, len(explained_variance) + 1),
    explained_variance,
    alpha=0.7,
    label="Individual Explained Variance"
)
plt.plot(
    range(1, len(cumulative_variance) + 1),
    cumulative_variance,
    marker="o",
    label="Cumulative Explained Variance"
)
plt.title("Explained Variance by Principal Components (Iris Dataset)")
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.xticks(range(1, len(explained_variance) + 1))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/explained_variance.png")
plt.close()


# =========================================================
# 3. PCA visualization on Iris dataset (4D -> 2D)
# =========================================================
pca_iris = PCA(n_components=2)
X_iris_pca = pca_iris.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))

for class_idx, class_name in enumerate(target_names):
    plt.scatter(
        X_iris_pca[y == class_idx, 0],
        X_iris_pca[y == class_idx, 1],
        label=class_name,
        alpha=0.7
    )

plt.title("PCA on Iris Dataset (4D → 2D)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/pca_iris_2d_visualization.png")
plt.close()


# =========================================================
# 4. Console output
# =========================================================
print("=== Day 48: Dimensionality Reduction & PCA Intuition ===\n")

print("Synthetic 2D Data:")
print(f"Original shape: {X_2d.shape}")
print(f"Reduced shape after PCA (2D -> 1D): {X_2d_pca.shape}")
print(f"Explained variance ratio (PC1): {pca_2d.explained_variance_ratio_[0]:.4f}\n")

print("Iris Dataset:")
print(f"Original shape: {X.shape}")
print(f"Reduced shape after PCA (4D -> 2D): {X_iris_pca.shape}")
print("Explained variance ratio (all components):")
for i, ratio in enumerate(explained_variance, start=1):
    print(f"PC{i}: {ratio:.4f}")

print("\nCumulative explained variance:")
for i, ratio in enumerate(cumulative_variance, start=1):
    print(f"PC1 to PC{i}: {ratio:.4f}")

print("\nOutput images saved in 'outputs/' folder.")
