import pandas as pd

# Load the cleaned dataset
file_path = 'cleaned_dataset.csv'
data_cleaned = pd.read_csv(file_path)

# Option 1: Drop rows with missing values (if you prefer to remove them)
data_no_missing = data_cleaned.dropna()

# Option 2: Drop columns with missing values
# data_no_missing = data_cleaned.dropna(axis=1)

# Option 3: Fill missing values with a constant (e.g., 'Unknown')
data_filled_constant = data_cleaned.fillna('Unknown')

# Option 4: Fill missing values with column-wise strategies
# Fill numeric columns with the mean
data_cleaned_numeric_filled = data_cleaned.fillna(data_cleaned.mean(numeric_only=True))

# Fill categorical/text columns with the mode (most frequent value)
for column in data_cleaned.select_dtypes(include=['object']).columns:
    data_cleaned[column].fillna(data_cleaned[column].mode()[0], inplace=True)

# Check the result
print(data_cleaned.head())

# Optionally, save the processed dataset
data_cleaned.to_csv('final_dataset.csv', index=False)
