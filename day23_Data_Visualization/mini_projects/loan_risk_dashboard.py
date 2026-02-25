import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)

# Create dataset
df = pd.DataFrame({
    "Income": np.random.randint(20000, 100000, 100),
    "Loan_Amount": np.random.randint(5000, 50000, 100),
    "Credit_Score": np.random.randint(300, 850, 100)
})

# Create Risk Category
df["Risk"] = np.where(df["Credit_Score"] < 600, "High",
               np.where(df["Credit_Score"] < 700, "Medium", "Low"))

# --------------------------------
# Visualization Dashboard
# --------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12,10))

# 1️⃣ Scatter: Income vs Loan
axes[0,0].scatter(df["Income"], df["Loan_Amount"])
axes[0,0].set_title("Income vs Loan Amount")

# 2️⃣ Histogram: Credit Score
axes[0,1].hist(df["Credit_Score"], bins=10)
axes[0,1].set_title("Credit Score Distribution")

# 3️⃣ Boxplot: Loan by Risk
sns.boxplot(x="Risk", y="Loan_Amount", data=df, ax=axes[1,0])
axes[1,0].set_title("Loan Amount by Risk")

# 4️⃣ Heatmap
corr = df[["Income","Loan_Amount","Credit_Score"]].corr()
sns.heatmap(corr, annot=True, ax=axes[1,1])
axes[1,1].set_title("Correlation Matrix")

plt.tight_layout()
plt.show()
