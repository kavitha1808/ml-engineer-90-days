import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create dataset
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

sales = np.random.randint(20000, 50000, 12)
regions = np.random.choice(["North","South","East","West"], 100)
region_sales = np.random.randint(1000, 10000, 100)

df_sales = pd.DataFrame({
    "Month": months,
    "Monthly_Sales": sales
})

df_region = pd.DataFrame({
    "Region": regions,
    "Sales": region_sales
})

# -------------------------------
# Visualization
# -------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12,10))

# 1️⃣ Line Plot - Monthly Trend
axes[0,0].plot(df_sales["Month"], df_sales["Monthly_Sales"])
axes[0,0].set_title("Monthly Sales Trend")

# 2️⃣ Bar Plot - Monthly Sales
axes[0,1].bar(df_sales["Month"], df_sales["Monthly_Sales"])
axes[0,1].set_title("Monthly Sales Comparison")

# 3️⃣ Histogram - Sales Distribution
axes[1,0].hist(df_region["Sales"], bins=10)
axes[1,0].set_title("Regional Sales Distribution")

# 4️⃣ Seaborn Boxplot - Region Analysis
sns.boxplot(x="Region", y="Sales", data=df_region, ax=axes[1,1])
axes[1,1].set_title("Region-wise Sales Spread")

plt.tight_layout()
plt.show()
