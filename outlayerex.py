import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employees.csv")

# Look at salary column
print(df["Salary"].describe())

# Visualize and save as image
plt.boxplot(df["Salary"])
plt.title("Salary Distribution with Outliers")
plt.savefig("salary_outliers.png")  # <-- saves image
plt.close()

# Simple rule: mark salaries < 10000 or > 200000 as outliers
outliers = df[(df["Salary"] < 10000) | (df["Salary"] > 200000)]
print("Outliers found:\n", outliers)

# Remove them
df_clean = df[(df["Salary"] >= 10000) & (df["Salary"] <= 200000)]
print("Dataset shape before:", df.shape)
print("Dataset shape after removing outliers:", df_clean.shape)
