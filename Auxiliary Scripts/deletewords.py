# -*- coding: utf-8 -*-
"""deleteWords.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16Ks9IGH2af-VxQqOI0Ze2jgc0XMD1EjN
"""

from google.colab import files

# Ejecuta esta línea para abrir el selector de archivos y subir desde tu computadora
uploaded = files.upload()

# Esto cargará el archivo y lo guardará en el sistema de archivos temporal de Colab
# Los archivos estarán disponibles en el diccionario uploaded usando el nombre como clave

import pandas as pd

# Leer el archivo CSV
# Reemplaza 'nombre_del_archivo.csv' con el nombre de tu archivo
df = pd.read_csv(next(iter(uploaded)))

# Eliminar "Pregunta:" y "Respuesta:" de cada celda
df = df.replace({"Pregunta:": "", "Respuesta:": ""}, regex=True)

# Mostrar el DataFrame actualizado
print("DataFrame después de eliminar 'Pregunta:' y 'Respuesta:'")
print(df)

# Guardar el archivo CSV limpio
df.to_csv("archivo_limpio.csv", index=False)
print("Archivo limpio guardado como 'archivo_limpio.csv'")