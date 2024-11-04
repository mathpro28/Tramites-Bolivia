import pandas as pd

def add_quotes_to_columns(input_file, output_file):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Convert all columns to string type first
        df = df.astype(str)
        
        # Remove any existing quotes first
        for column in df.columns:
            df[column] = df[column].str.replace('"', '')
        
        # Save to CSV with proper quoting
        df.to_csv(output_file, index=False, quoting=1, quotechar='"', escapechar='\\')
        print(f"Successfully added quotes to all columns and saved to: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_file = "cleaned_output.csv"  # Replace with your input CSV file path
    output_file = "quoted_output.csv"  # Replace with your desired output file path
    
    add_quotes_to_columns(input_file, output_file)