import pandas as pd

# Load the dataset
file_path = 'final.csv'  # Adjust this to your actual file path
df = pd.read_csv(file_path)

# Replace all empty cells (NaN) with "Desconocido"
df.fillna("Desconocido", inplace=True)

# Save the modified dataset to a new CSV file
output_path = 'tramites.csv'
df.to_csv(output_path, index=False)

print("Empty cells filled with 'Desconocido' and file saved.")
