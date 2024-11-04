import pandas as pd
from bs4 import BeautifulSoup

# Load your CSV file
file_path = 'tramites_rev.csv'
data = pd.read_csv(file_path, delimiter='|', on_bad_lines='skip')

# Function to remove HTML tags
def remove_html_tags(text):
    # Check if the value is not NaN
    if isinstance(text, str):
        # Parse and remove HTML tags
        return BeautifulSoup(text, "html.parser").get_text()
    return text

# Apply the function to all columns in the DataFrame
data_cleaned = data.applymap(remove_html_tags)

# Check the cleaned result
print(data_cleaned.head())

# Optionally, save the cleaned dataset to a new CSV
data_cleaned.to_csv('cleaned_dataset.csv', index=False)
