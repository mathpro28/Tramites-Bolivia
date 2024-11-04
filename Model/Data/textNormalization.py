import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load your dataset
file_path = 'final_dataset_with_flattened_json.csv'
data_cleaned = pd.read_csv(file_path)

# Function to replace accented letters with base forms
def remove_accents(text):
    accents_map = str.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU')
    return text.translate(accents_map)

# Function to normalize text with lemmatization and accent removal (Spanish)
def normalize_text(text):
    # 1. Convert text to lowercase
    text = text.lower()
    
    # 2. Remove accents from the text
    text = remove_accents(text)
    
    # 3. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 4. Remove special characters and numbers
    text = re.sub(r'\d+', '', text)
    
    # 5. Tokenize the text
    tokens = word_tokenize(text)
    
    # 6. Remove stopwords (in Spanish)
    stop_words = set(stopwords.words('spanish'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # 7. Lemmatization (Spanish)
    lemmatizer = WordNetLemmatizer()  # Substitute with a Spanish lemmatizer if available
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join tokens back into a single string
    return ' '.join(tokens)

# List of columns containing text to normalize
text_columns = [
    'objetivo_entidad', 'mecanismos_seguimiento', 'mecanismos_atencion', 
    'proyectos_simplificacion', 'experiencia_ciudadana', 'objetivo_tramite', 
    'palabras_clave', 'procedimientos', 'observacion_tramite'
]

# Apply normalization to each text column
for col in text_columns:
    data_cleaned[col] = data_cleaned[col].apply(lambda x: normalize_text(x) if isinstance(x, str) else x)

# Save the lemmatized and accent-corrected dataset
data_cleaned.to_csv('lemmatized_accent_corrected_dataset.csv', index=False)
