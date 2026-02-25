import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create dataset
np.random.seed(42)

data = {
    "Hours_Studied": np.random.randint(1, 10, 30),
    "Attendance (%)": np.random.randint(60, 100, 30),
}

df = pd.DataFrame(data)

# Create Marks based on hours + attendance
df["Marks"] = df["Hours_Studied"] * 8 + df["Attendance (%)"] * 0.5 + np.random.randint(-5,5,30)

# -------------------------------
# Visualization
# -------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12,10))

# 1️⃣ Line Plot
axes[0,0].plot(df["Hours_Studied"], df["Marks"])
axes[0,0].set_title("Hours vs Marks")

# 2️⃣ Scatter Plot
axes[0,1].scatter(df["Attendance (%)"], df["Marks"])
axes[0,1].set_title("Attendance vs Marks")

# 3️⃣ Histogram
axes[1,0].hist(df["Marks"], bins=8)
axes[1,0].set_title("Marks Distribution")

# 4️⃣ Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, ax=axes[1,1])
axes[1,1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.show()
