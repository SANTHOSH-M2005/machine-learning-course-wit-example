import pandas as pd
from sklearn.model_selection import train_test_split

# Step 1: Load dataset
df = pd.read_csv("students.csv")

# Step 2: Features (Age, Marks) and Label (Passed)
X = df[["Age", "Marks"]]   # Features
y = df["Passed"]           # Label

# Step 3: Split into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Print the results
print("Training set:")
print(X_train)
print(y_train)

print("\nTesting set:")
print(X_test)
print(y_test)
