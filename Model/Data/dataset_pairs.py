import pandas as pd

# load data set
df_final = pd.read_csv('dataset_QA.csv')


data = []

# Process each row
for _, row in df_final.iterrows():
    pregunta = row['pregunta']
    respuesta = row['respuesta']
    data.append({"input_text": f"Pregunta: {pregunta} Respuesta:", "target_text": respuesta})

# list to data frame
df_pairs = pd.DataFrame(data)

# save dataframe
df_pairs.to_csv('dataset_pairs.csv', index=False, encoding='utf-8')

print("Transformación completada y guardada en 'dataset_pairs.csv'")
