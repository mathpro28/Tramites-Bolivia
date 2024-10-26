import pandas as pd
from datetime import datetime

# Load the dataset
file_path = 'new_csv.csv'  # Adjust the path to your actual file
df = pd.read_csv(file_path)

# Define the columns to normalize
time_columns = ['primero.hora_fin', 'primero.hora_ini', 'segundo.hora_fin', 'segundo.hora_ini']

# Function to convert datetime to 12-hour format and only show the time
def normalize_time(time_str):
    try:
        # Convert the string to a datetime object
        time_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        # Return the time in 12-hour format
        return time_obj.strftime('%I:%M %p')
    except Exception as e:
        print(f"Error processing {time_str}: {e}")
        return time_str

# Apply the function to the time columns
for col in time_columns:
    df[col] = df[col].apply(normalize_time)

# Save the updated dataset
output_path = 'final.csv'  # Adjust the path to your output file
df.to_csv(output_path, index=False)

print("Time columns successfully normalized and file saved.")
