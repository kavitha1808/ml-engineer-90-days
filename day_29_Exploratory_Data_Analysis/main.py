import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.eda_functions import basic_info, summary_statistics, correlation_matrix

# Create output folder if not exists
os.makedirs("outputs/plots", exist_ok=True)

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# -----------------------------
# 1️⃣ Basic Structure Analysis
# -----------------------------
basic_info(df)

# -----------------------------
# 2️⃣ Statistical Summary
# -----------------------------
summary_statistics(df)

# -----------------------------
# 3️⃣ Histogram – Marks Distribution
# -----------------------------
plt.figure()
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("outputs/plots/marks_histogram.png")
plt.close()

# -----------------------------
# 4️⃣ Boxplot – Outlier Detection
# -----------------------------
plt.figure()
sns.boxplot(y=df["Marks"])
plt.title("Marks Boxplot")
plt.savefig("outputs/plots/marks_boxplot.png")
plt.close()

# -----------------------------
# 5️⃣ Scatter – Study Hours vs Marks
# -----------------------------
plt.figure()
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.savefig("outputs/plots/study_vs_marks.png")
plt.close()

# -----------------------------
# 6️⃣ Scatter – Sleep vs Marks
# -----------------------------
plt.figure()
plt.scatter(df["Sleep_Hours"], df["Marks"])
plt.xlabel("Sleep Hours")
plt.ylabel("Marks")
plt.title("Sleep vs Marks")
plt.savefig("outputs/plots/sleep_vs_marks.png")
plt.close()

# -----------------------------
# 7️⃣ Correlation Heatmap
# -----------------------------
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Matrix")
plt.savefig("outputs/plots/correlation_heatmap.png")
plt.close()

print("\nEDA Completed Successfully!")
print("Plots saved inside outputs/plots/")
