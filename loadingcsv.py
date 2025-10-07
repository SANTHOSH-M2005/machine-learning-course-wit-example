# Step 1: Import pandas
import pandas as pd

# Step 2: Load the dataset (make sure students.csv is in the same folder as this script)
df = pd.read_csv("students.csv")

# Step 3: View the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 4: Separate features and label
features = df[["Age", "Salary", "Hours_Studied"]]
label = df["Passed"]

print("\nFeatures (X):")
print(features.head())

print("\nLabel (y):")
print(label.head())
