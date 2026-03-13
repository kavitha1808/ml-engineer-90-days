# distance_metrics_demo.py

import numpy as np
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Two points
A = np.array([2, 3])
B = np.array([5, 7])

# Euclidean distance
euclidean = np.linalg.norm(B - A)

# Manhattan distance
manhattan = np.sum(np.abs(B - A))

# Minkowski distance (p=3 example)
p = 3
minkowski = np.sum(np.abs(B - A) ** p) ** (1 / p)

print("Point A:", A)
print("Point B:", B)
print(f"Euclidean Distance: {euclidean:.2f}")
print(f"Manhattan Distance: {manhattan:.2f}")
print(f"Minkowski Distance (p=3): {minkowski:.2f}")

# Plot points
plt.figure(figsize=(6, 6))
plt.scatter(A[0], A[1], label='Point A', s=100)
plt.scatter(B[0], B[1], label='Point B', s=100)

# Draw Euclidean line
plt.plot([A[0], B[0]], [A[1], B[1]], linestyle='--', label='Euclidean Path')

# Draw Manhattan path
plt.plot([A[0], B[0]], [A[1], A[1]], linestyle=':', label='Manhattan Path 1')
plt.plot([B[0], B[0]], [A[1], B[1]], linestyle=':')

plt.title("Distance Metrics Visualization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.savefig("outputs/distance_metrics_plot.png")
plt.show()
