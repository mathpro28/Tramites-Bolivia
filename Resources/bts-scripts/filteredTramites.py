import pandas as pd

def filter_csv_columns(input_file, output_file):
    # Columns to keep
    columns_to_keep = [
        'organization_id',
        'denominacion',
        'sigla',
        'objetivo_entidad',
        'url_sitio_web',
        'procedure_id',
        'descripcion_categoria',
        'continuo',
        'primero.hora_ini',
        'primero.hora_fin',
        'segundo.hora_ini',
        'segundo.hora_fin'
    ]

    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Select only the specified columns
        # If a column doesn't exist, it will be ignored without raising an error
        existing_columns = [col for col in columns_to_keep if col in df.columns]
        filtered_df = df[existing_columns]
        
        # Save the filtered dataframe to a new CSV file
        filtered_df.to_csv(output_file, index=False)
        print(f"Successfully created filtered CSV file: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_file = "tramites_50_db.csv"  # Replace with your input CSV file path
    output_file = "filtered_output2.csv"  # Replace with your desired output file path
    
    filter_csv_columns(input_file, output_file)