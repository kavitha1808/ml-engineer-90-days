import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Marks": [35,40,50,60,65,70,80,90]
}

df = pd.DataFrame(data)

fig, axes = plt.subplots(2, 2, figsize=(10,8))

axes[0,0].plot(df["Hours_Studied"], df["Marks"])
axes[0,0].set_title("Line")

axes[0,1].scatter(df["Hours_Studied"], df["Marks"])
axes[0,1].set_title("Scatter")

axes[1,0].hist(df["Marks"], bins=5, edgecolor="black")
axes[1,0].set_title("Histogram")

sns.heatmap(df.corr(), annot=True, ax=axes[1,1])
axes[1,1].set_title("Heatmap")

plt.tight_layout()
plt.show()
