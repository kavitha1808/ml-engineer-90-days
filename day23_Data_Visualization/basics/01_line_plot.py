import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Marks": [35,40,50,60,65,70,80,90]
}

df = pd.DataFrame(data)

# Matplotlib
plt.figure()
plt.plot(df["Hours_Studied"], df["Marks"])
plt.title("Line Plot - Matplotlib")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()

# Seaborn
plt.figure()
sns.lineplot(x="Hours_Studied", y="Marks", data=df)
plt.title("Line Plot - Seaborn")
plt.show()
