import pandas as pd

# Load the data
df = pd.read_csv("data/heart.csv")

# Look at the first 5 rows
print("--- First 5 Rows ---")
print(df.head())

# Check for missing values
print("\n--- Missing Values ---")
print(df.isna().sum())

# See the distribution of the target (1 = heart disease, 0 = no disease)
print("\n--- Heart Disease Count (Target) ---")
print(df['target'].value_counts())
