import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Marks": [35,40,50,60,65,70,80,90]
}

df = pd.DataFrame(data)

plt.figure()
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Scatter - Matplotlib")
plt.show()

plt.figure()
sns.scatterplot(x="Hours_Studied", y="Marks", data=df)
plt.title("Scatter - Seaborn")
plt.show()
