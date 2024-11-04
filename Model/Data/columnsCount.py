import pandas as pd

# Load the CSV file
file_path = 'tramites.csv'
df = pd.read_csv(file_path)

# Get the number of columns
num_columns = df.shape[1]
num_columns

print(num_columns)

