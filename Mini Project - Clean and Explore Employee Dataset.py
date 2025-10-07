import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
df =pd.read_csv("employee_practice.csv") # <-- Fill: load CSV file 
print("First 5 rows:\n", df.head())

# -----------------------------
# Step 2: Identify Features & Label and Print features columns and label name
# -----------------------------
features = df.drop("Promotion_Eligibility", axis=1)  
label = df["Promotion_Eligibility"]  

print("\nFeatures:\n", features.columns)  # <-- Fill: print feature columns 
print("Label:\n",label.name)   # <-- Fill: print label name 

# -----------------------------
# Step 3: Handle Missing Values
# -----------------------------
print("\nMissing Values Before:\n", df.isnull().sum())  # <-- Fill: check missing values 

# Fill numerical missing values with median
df["Age"] = df["Age"].fillna(df['Age'].mean())  # <-- Fill: handle missing Age 
df["Years_Experience"] = df["Years_Experience"].fillna(df['Years_Experience'].mean()) # <-- Fill: handle missing Years_Experience 

# Fill categorical missing values with mode
df["Department"] = df["Department"].fillna(df['Department'].mode()[0])  # <-- Fill: handle missing Department 
df["Promotion_Eligibility"] = df["Promotion_Eligibility"].fillna(df['Promotion_Eligibility'].mode()[0])  # <-- Fill: handle missing Promotion_Eligibility 

print("\nMissing Values After:\n", df.isnull().sum())

# -----------------------------
# Step 4: Detect & Handle Outliers (Simple Method)
# -----------------------------
# Identify Salary outliers (e.g., Salary < 30000 or Salary > 150000)
salary_outliers = df[(df["Salary"] < 30000) | (df["Salary"] > 150000)]  # <-- Fill: set low and high threshold values
print("\nSalary Outliers:\n", salary_outliers)

# Remove Salary outliers 
df = df[(df["Salary"] >= 30000) & (df["Salary"] <= 150000) ]

# Handle Years_Experience outliers (remove > 30 years)
df = df[(df["Years_Experience"]) <=30]


# -----------------------------
# Step 5: Handling Outliers
# -----------------------------
print("\nDescriptive Statistics:\n", df.describe())  # <-- Fill: get descriptive stats 
print("\nEmployees per Department:\n", df["Department"].value_counts())  # <-- Fill: count employees 

plt.figure(figsize=(6,4))
plt.boxplot(df["Salary"])  # <-- Fill: column to visualize "Salary"
plt.title("Salary Distribution After Handling Outliers")
plt.ylabel("Salary")   # <-- Fill: y-axis label ("Salary")
plt.savefig("salary_boxplot.png")  # Save the image
plt.show()

