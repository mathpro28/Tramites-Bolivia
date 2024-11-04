import csv

def create_limited_csv(input_file, output_file, row_limit=50):
    # Open the input file
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        # Open the output file
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            # Write the first row (headers) to the output file
            headers = next(reader)
            writer.writerow(headers)
            # Write only the specified number of rows
            for i, row in enumerate(reader):
                if i < row_limit:
                    writer.writerow(row)
                else:
                    break

# Usage example:
create_limited_csv('new_tramites_modified.csv', 'tramites_50_db.csv')
