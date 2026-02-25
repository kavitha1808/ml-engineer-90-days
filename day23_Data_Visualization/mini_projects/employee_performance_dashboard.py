import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1)

# Create dataset
df = pd.DataFrame({
    "Experience (Years)": np.random.randint(1, 15, 80),
    "Projects": np.random.randint(1, 20, 80),
    "Salary": np.random.randint(30000, 150000, 80),
    "Performance_Rating": np.random.randint(1, 6, 80)
})

# --------------------------------
# Visualization Dashboard
# --------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12,10))

# 1️⃣ Line Plot
axes[0,0].plot(df["Experience (Years)"], df["Salary"])
axes[0,0].set_title("Experience vs Salary")

# 2️⃣ Scatter Plot
axes[0,1].scatter(df["Projects"], df["Performance_Rating"])
axes[0,1].set_title("Projects vs Performance")

# 3️⃣ Histogram
axes[1,0].hist(df["Salary"], bins=10)
axes[1,0].set_title("Salary Distribution")

# 4️⃣ Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, ax=axes[1,1])
axes[1,1].set_title("Correlation Matrix")

plt.tight_layout()
plt.show()
