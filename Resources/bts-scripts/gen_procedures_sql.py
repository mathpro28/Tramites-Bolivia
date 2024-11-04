import pandas as pd
from datetime import datetime
import random

# Load the CSV file
file_path = '/Users/mateo/Downloads/time_columns.csv'
df = pd.read_csv(file_path)

# Function to generate random time in HH:MM:SS format
def generate_random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return f"{hour:02}:{minute:02}:00"

# Function to format time from AM/PM to 24-hour format, handling empty or default values
def format_time(time_str):
    if time_str.strip() == '' or time_str == '00:00:00':
        return generate_random_time()
    try:
        # Convert AM/PM time to 24-hour format
        dt = datetime.strptime(time_str.strip(), '%I:%M %p')
        return dt.strftime('%H:%M:%S')
    except ValueError:
        return generate_random_time()  # Use random time for incorrect formats

# Initialize organization ID counter
organization_id_counter = 1

# Update insert statements with formatted time and boolean values for `continuo`
updated_insert_statements = []

# First, ensure that there are organizations to link to
organizations_insert_statements = []

# Assuming a fixed organization for demonstration
# You can customize this part to match your actual organization data.
for org_id in range(1, organization_id_counter + len(df)):  # Adjust as needed
    organizations_insert_statements.append(f"INSERT INTO organizations (organization_id, organization_name) VALUES ({org_id}, 'Organization {org_id}');")

# Prepare procedure insert statements
for _, row in df.iterrows():
    # Generate or increment the organization ID
    organization_id = organization_id_counter
    organization_id_counter += 1

    descripcion_categoria = row['descripcion_categoria'].replace("'", "''")
    continuo = '1' if row['continuo'].strip().lower() == 'true' else '0'
    
    # Generate random times for each time-related column
    primero_hora_ini = format_time(row['primero_hora_ini'])
    primero_hora_fin = format_time(row['primero_hora_fin'])
    segundo_hora_ini = format_time(row['segundo_hora_ini'])
    segundo_hora_fin = format_time(row['segundo_hora_fin'])
    
    insert_statement = (
        f"INSERT INTO procedures (organization_id, descripcion_categoria, continuo, primero_hora_ini, primero_hora_fin, "
        f"segundo_hora_ini, segundo_hora_fin) VALUES ({organization_id}, '{descripcion_categoria}', {continuo}, "
        f"'{primero_hora_ini}', '{primero_hora_fin}', '{segundo_hora_ini}', '{segundo_hora_fin}');"
    )
    updated_insert_statements.append(insert_statement)

# Save the corrected INSERT statements to a new text file
corrected_output_file_path = 'corrected_insert_procedure_statements2.sql'

with open(corrected_output_file_path, 'w') as file:
    for statement in organizations_insert_statements:
        file.write(statement + '\n')
    for statement in updated_insert_statements:
        file.write(statement + '\n')

corrected_output_file_path
