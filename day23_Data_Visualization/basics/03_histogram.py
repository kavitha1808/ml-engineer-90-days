import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=20, edgecolor="black")
plt.title("Histogram - Matplotlib")
plt.show()

plt.figure()
sns.histplot(data, bins=20, edgecolor="black")
plt.title("Histogram - Seaborn")
plt.show()
