import pandas as pd

# Load the dataset
file_path = 'lemmatized_accent_corrected_dataset.csv'  # Adjust the path to your actual file
df = pd.read_csv(file_path)

# List of columns to drop
columns_to_drop = ['codigo', 'mecanismos_seguimiento', 'experiencia_ciudadana', 'horario_atencion_tramite', 
                   'duracion_tramite', '0', '1', '2', '3', '4', '5', '6', '7', '8']

# Drop the specified columns
df = df.drop(columns=columns_to_drop, errors='ignore')

# Save the updated dataset back to CSV
output_path = 'new_csv.csv'  # Adjust the path to your output file
df.to_csv(output_path, index=False)

print("Columns successfully deleted and file saved.")
