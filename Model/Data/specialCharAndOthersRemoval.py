import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to clean text
def cleanText(text):
    # Remove special characters except ! and ?
    cleanedText = re.sub(r'[^a-zA-Z0-9!? ]+', '', text)
    # Remove [U+32] explicitly if present
    cleanedText = cleanedText.replace('\u0020', '')  # Unicode for [U+32] is space
    return cleanedText