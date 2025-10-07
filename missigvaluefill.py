import pandas as pd

def handle_missing_values(file_path):

    # Step 1: Load dataset
    df = pd.read_csv("students.csv")
    print("Original Dataset:")
    print(df.head())

    # Step 2: Check missing values
    print("\nMissing Values per Column:")
    print(df.isnull().sum())

    # Step 3: Fill missing numerical values with mean
    df['Math_Score'] =df['Math_Score'].fillna(df['Math_Score'].mean())
    df['English_Score'] = df['English_Score'].fillna(df['English_Score'].mean())
    df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].mean())

    # Step 4: Fill missing categorical values with mode
    df['Class'] = df['Class'].fillna(df['Class'].mode()[0])

    # Step 5: Round numerical columns to 1 decimal place
    df[['Math_Score', 'English_Score', 'Science_Score']] = df[['Math_Score', 'English_Score', 'Science_Score']].round(1)

    # Step 6: Display dataset after handling missing values
    print("\nDataset after Handling Missing Values (rounded to 1 decimal):")
    print(df.head())

    return df

# Call the function in main
if __name__ == "__main__":
    handle_missing_values("students.csv")
