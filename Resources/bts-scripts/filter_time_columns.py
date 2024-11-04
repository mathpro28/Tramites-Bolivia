import pandas as pd

def filter_time_columns(input_file, output_file):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Print all column names to check exact names
        print("Available columns in CSV:")
        for col in df.columns:
            print(f"'{col}'")
            
        # Columns we want to keep
        columns_to_keep = [
            'descripcion_categoria',
            'continuo',
            'primero.hora_ini',
            'primero.hora_fin',
            'segundo.hora_ini',
            'segundo.hora_fin'
        ]
        
        # Check which columns exist
        existing_columns = [col for col in columns_to_keep if col in df.columns]
        missing_columns = [col for col in columns_to_keep if col not in df.columns]
        
        print("\nFound columns:", existing_columns)
        print("Missing columns:", missing_columns)
        
        if existing_columns:
            # Select only the existing columns
            filtered_df = df[existing_columns]
            filtered_df.to_csv(output_file, index=False, quoting=1)
            print(f"\nSuccessfully created filtered CSV with available columns: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_file = "tramites_50_db.csv"  # Replace with your input CSV file path
    output_file = "time_columns.csv"  # Replace with your desired output file path
    
    filter_time_columns(input_file, output_file)