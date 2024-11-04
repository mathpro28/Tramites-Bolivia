import pandas as pd

# Nombre del archivo CSV de entrada y de salida
input_file = 'dataset_guanaco.csv'  # Archivo de entrada sin encabezado
output_file = 'dataset_con_encabezado.csv'  # Archivo de salida con encabezado

# Cargar el archivo CSV sin encabezado
df = pd.read_csv(input_file, header=None, names=['text'])

# Guardar el archivo con el encabezado
df.to_csv(output_file, index=False)

print(f"Archivo con encabezado guardado como {output_file}")
