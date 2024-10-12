import csv
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def removeHtmlTags(inputString):
    # Check if inputString is indeed a string and looks like it might contain HTML
    if isinstance(inputString, str) and '<' in inputString and '>' in inputString:
        soup = BeautifulSoup(inputString, 'html.parser')
        return soup.get_text()
    # If inputString doesn't look like HTML, return it unchanged
    return inputString

def cleanCSVColumn(inputCSVPath, outputCSVPath, columnIndex):
    with open(inputCSVPath, mode='r', encoding='utf-8') as infile, \
         open(outputCSVPath, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row:  # Check if row is not empty
                # Clean the HTML content in the specified column
                row[columnIndex] = removeHtmlTags(row[columnIndex])
            writer.writerow(row)