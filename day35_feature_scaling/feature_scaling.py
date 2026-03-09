import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Sample dataset
data = {
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# -----------------------------
# Normalization (MinMax Scaling)
# -----------------------------
minmax = MinMaxScaler()
normalized_data = minmax.fit_transform(df)

normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

print("\nNormalized Data")
print(normalized_df)

# -----------------------------
# Standardization (Z-score)
# -----------------------------
standard = StandardScaler()
standardized_data = standard.fit_transform(df)

standardized_df = pd.DataFrame(standardized_data, columns=df.columns)

print("\nStandardized Data")
print(standardized_df)

# -----------------------------
# Visualization
# -----------------------------
plt.scatter(df["Age"], df["Salary"], label="Original Data")
plt.scatter(normalized_df["Age"], normalized_df["Salary"], label="Normalized Data")
plt.scatter(standardized_df["Age"], standardized_df["Salary"], label="Standardized Data")

plt.title("Feature Scaling Comparison")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()

plt.savefig("outputs/scaling_visualization.png")
plt.show()
