import pandas as pd
import re

# Load your cleaned dataset
file_path = 'final_dataset_with_flattened_json.csv'
data_cleaned = pd.read_csv(file_path)

# Function to remove Unicode symbols
def remove_unicode_symbols(text):
    # Use regular expressions to remove non-ASCII characters (Unicode symbols)
    if isinstance(text, str):
        # Replace anything that's not ASCII (0-127) with an empty string
        return re.sub(r'[^\x00-\x7F]+', '', text)
    return text

# List of columns containing text to clean
text_columns = [
    'objetivo_entidad', 'mecanismos_seguimiento', 'mecanismos_atencion', 
    'proyectos_simplificacion', 'experiencia_ciudadana', 'objetivo_tramite', 
    'palabras_clave', 'procedimientos', 'observacion_tramite'
]

# Apply the remove_unicode_symbols function to each text column
for col in text_columns:
    data_cleaned[col] = data_cleaned[col].apply(remove_unicode_symbols)

# Check the result
print(data_cleaned[text_columns].head())

# Optionally, save the processed dataset
data_cleaned.to_csv('dataset_without_unicode.csv', index=False)
