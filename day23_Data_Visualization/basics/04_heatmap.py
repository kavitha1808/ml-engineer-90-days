import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Marks": [35,40,50,60,65,70,80,90]
}

df = pd.DataFrame(data)

corr = df.corr()

plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
