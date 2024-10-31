import pandas as pd

# Cargar el dataset en un DataFrame
df = pd.read_csv('new_tramites.csv')

# Crear una lista para almacenar los datos en el formato requerido
data = []

# Procesar cada fila para crear el formato SQuAD
for _, row in df.iterrows():
    titulo = row['titulo_tramite']
    objetivo = row['objetivo_tramite']
    procedimientos = row['procedimientos']
    duracion_meses = row['duracion_meses']
    duracion_dias = row['duracion_dias']
    duracion_horas = row['duracion_horas']
    duracion_minutos = row['duracion_minutos']
    costo = row['monto_costo']
    url = row['url_sitio_web']
    
    # Crear el contexto
    contexto = (f"El objetivo del trámite es {objetivo}. "
                f"El procedimiento que se debe realizar es {procedimientos}. "
                f"La duración del trámite es de {duracion_meses} meses, {duracion_dias} días, "
                f"{duracion_horas} horas y {duracion_minutos} minutos. "
                f"El trámite tiene un costo de Bs. {costo}. "
                f"Para más información visitar el sitio {url}.")
    
    # Preguntas y respuestas
    preguntas = [
        f"¿Qué pasos debo seguir para realizar el trámite {titulo}?",
        f"¿Qué duración tiene el trámite {titulo}?",
        f"¿Qué costo tiene el trámite {titulo}?",
        f"¿Cuál es el objetivo del trámite {titulo}?"
    ]
    
    respuestas = [
        procedimientos,
        f"{duracion_meses} meses, {duracion_dias} días, {duracion_horas} horas, {duracion_minutos} minutos.",
        f"Bs. {costo}.",
        objetivo
    ]
    
    for pregunta, respuesta in zip(preguntas, respuestas):
        data.append({
            "titulo": titulo,
            "contexto": contexto,
            "pregunta": pregunta,
            "respuesta": respuesta
        })

# Convertir la lista a un DataFrame
df_final = pd.DataFrame(data)

# Guardar el nuevo DataFrame en un archivo CSV
df_final.to_csv('dataset_QA.csv', index=False, encoding='utf-8')

print("Transformación completada y guardada en 'dataset_squad.csv'")
