import os
import pandas as pd
from dotenv import load_dotenv 

from lemmatization import lemmatizer
from stopWords import removeStopWords
from filtering import convertNumberWords
from StripCharsSpaces import singleCharacterRemoval, specialCharacterRemoval, removeMultipleSpaces


if __name__ == "__main__":
    # Import filtered and distributed data
    load_dotenv() 
    FILTERED_DATA_PATH = os.getenv("FILTERED_DATA_PATH")
    df = pd.read_csv(FILTERED_DATA_PATH)
    
    # Apply functions:
    # Stop Words Removal
    df['text'] = df['text'].apply(removeStopWords)
    df['title'] = df['title'].apply(removeStopWords)

    # Lemmatization:
    df['text'] = df['text'].apply(lemmatizer)
    df['title'] = df['title'].apply(lemmatizer)

    # Single Characters Removal
    df['text'] = df['text'].apply(singleCharacterRemoval)
    df['title'] = df['title'].apply(singleCharacterRemoval)

    # Convert words to numbers
    df['text'] = df['text'].apply(convertNumberWords)
    df['title'] = df['title'].apply(convertNumberWords)
    
    # Special Characteres Removal
    specialCharactersToRemove = [
    '~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"',
    "'", '<', '>', ',', '.', '/', '-', '\n', '\t', '\r', '\x0b', '\x0c']
    df['text'] = df['text'].apply(lambda x: specialCharacterRemoval(x, specialCharactersToRemove))
    df['title'] = df['title'].apply(lambda x: specialCharacterRemoval(x, specialCharactersToRemove))

    # Multiples Spaces Removal
    df['text'] = df['text'].apply(removeMultipleSpaces)
    df['title'] = df['title'].apply(removeMultipleSpaces)

    # Columns selection
    df = df[['title', 'text', 'overall']]

    # Generate preprocessed csv file
    PREPROCESSED_DATA_PATH = os.getenv('PREPROCESSED_DATA_PATH')
    df.to_csv(PREPROCESSED_DATA_PATH, index=False)  
