import pandas as pd
import json

# Load your cleaned dataset
file_path = 'final_dataset.csv'
data_cleaned = pd.read_csv(file_path)

# Function to flatten JSON fields
def flatten_json_column(df, column_name):
    # Convert the JSON-like string into a Python dictionary
    df[column_name] = df[column_name].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
    
    # Flatten the JSON column
    flattened = pd.json_normalize(df[column_name])
    
    # Concatenate the flattened columns back to the original DataFrame
    df = pd.concat([df.drop(columns=[column_name]), flattened], axis=1)
    return df

# List the columns with nested JSON structures
json_columns = ['horario_atencion_entidad', 'servicios_intercambio']  # Replace with actual columns containing JSON

# Loop through each JSON column and flatten it
for col in json_columns:
    data_cleaned = flatten_json_column(data_cleaned, col)

# Check the result
print(data_cleaned.head())

# Optionally, save the processed dataset
data_cleaned.to_csv('final_dataset_with_flattened_json.csv', index=False)
