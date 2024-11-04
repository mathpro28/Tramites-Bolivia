import pandas as pd

# Load the dataset
file_path = 'tramites.csv'  # Adjust the path to your actual file
df = pd.read_csv(file_path)

# List of columns to drop
columns_to_drop = ['mecanismos_atencion', 'proyectos_simplificacion', 'valoracion', 'tipo_acceso', 'concepto_costo']

# Drop the specified columns
df = df.drop(columns=columns_to_drop, errors='ignore')

# Save the updated dataset back to CSV
output_path = 'new_tramites.csv'  # Adjust the path to your output file
df.to_csv(output_path, index=False)

print("Columns successfully deleted and file saved.")
