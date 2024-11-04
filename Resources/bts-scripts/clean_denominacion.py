import pandas as pd

def clean_denominacion(input_file, output_file):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Clean the denominacion column by removing quotes and commas
        df['denominacion'] = df['denominacion'].str.replace('"', '', regex=False)
        df['denominacion'] = df['denominacion'].str.replace(',', '', regex=False)
        
        # Save the cleaned dataframe back to CSV
        df.to_csv(output_file, index=False)
        print(f"Successfully cleaned denominacion column and saved to: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_file = "filtered_output.csv"  # Replace with your input CSV file path
    output_file = "cleaned_output.csv"  # Replace with your desired output file path
    
    clean_denominacion(input_file, output_file)