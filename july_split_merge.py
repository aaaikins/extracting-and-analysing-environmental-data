"""
Name of File: july_split_merge.py
Date: 09/20/2023
Author's Name: Aikins Acheampong

Purpose: this program extracts July data from two different CSV files(Goldie2019.csv and MLRCWeather2019.csv), filters them and then zips the data into a single CSV file(MLRC2019JulyFiltered.csv)

"""

def clearfile(filename):
    """
    Clears the content of the specified file.
    """
    fp = open(filename, 'w')
    fp.close()  


gold19 = open('Goldie2019.csv', 'r')  # Open Goldie2019.csv in read mode
new_csv = ""  # Initialize an empty string to store new CSV data
lines_of_text = gold19.readlines()  # Read all lines from Goldie2019.csv

for line in lines_of_text[2:3]:  # Iterate over a slice of lines (2nd line only) and append the line to new_csv
    new_csv += line

size = len(lines_of_text)  # Get the total number of lines in the file

for i in range(size - 4):  # Iterate through the lines (excluding the last 2), Split the line into a list of values, Split date into [mm, dd, yyyy], Check if the month is '07', Append the line to new_csv
    line = lines_of_text[i].split(",")
    mm_dd_yyyy = line[0].split('/')

    if mm_dd_yyyy[0] == '07':  
        new_csv += lines_of_text[i]  

clearfile('Goldie2019July.csv')  # Clear content of Goldie2019July.csv

with open("Goldie2019July.csv", "w") as new_file:  # Open Goldie2019July.csv in write mode and Write new_csv content to the file
    new_file.write(new_csv)


mlrc19 = open('MLRCWeather2019.csv', 'r')  # Open MLRCWeather2019.csv in read mode
new_csv = ""  # Initialize an empty string to store new CSV data
lines_of_text = mlrc19.readlines()  # Read all lines from MLRCWeather2019.csv

for line in lines_of_text[:1]:  # Iterate over the first line only and append the line to new_csv
    new_csv += line

size = len(lines_of_text)  # Get the total number of lines in the file

for i in range(size - 2):  # Iterate through the lines (excluding the last line), split the line into a list of values, Split date into [mm, dd, yyyy], Check if the month is '07' and Append the line to new_csv
    line = lines_of_text[i].split(",")
    mm_dd_yyyy = line[0].split('/')

    if mm_dd_yyyy[0] == '07':
        new_csv += lines_of_text[i]  

clearfile('MLRC2019July.csv')  # Clear content of MLRC2019July.csv

new_file = open("MLRC2019July.csv", "w")  # Open MLRC2019July.csv in write mode
new_file.write(new_csv)  # Write new_csv content to the file


def extract_columns(input_filename, output_filename, columns_to_extract):
    """
    Extracts specified columns from the input file and writes them to the output file.
    """
    input_file = open(input_filename, 'r')  # Open the input file in read mode
    lines = input_file.readlines()  # Read all lines from the input file
    filtered_data = []  # Initialize an empty list to store filtered data
    selected_columns = []

    for line in lines:  # Iterate over each line in the input file
        columns = line.split(',')  # Split line into a list of values
        selected_columns =[columns[i] for i in columns_to_extract]  # Select specified columns
        filtered_data.append(','.join(selected_columns))  # Join selected columns and append to filtered_data

    output_file = open(output_filename, 'w')  # Open the output file in write mode
    output_file.write('\n'.join(filtered_data))  # Write filtered data to the output file



extract_columns('Goldie2019July.csv', 'Goldie2019JulyFiltered.csv', [0, 11, 16, 17, 21])  # Extract columns from Goldie2019July.csv
extract_columns('MLRC2019July.csv', 'MLRC2019JulyFiltered.csv', [2, 5, 7])  # Extract columns from MLRC2019July.csv


def zip_files(file1, file2, output_filename):
    """
    Zips the content of two files together and writes to an output file.
    """
    with open(file1, 'r') as file1, open(file2, 'r') as file2, open(output_filename, 'w') as output_file:
        lines1 = file1.readlines()  # Read all lines from the first file
        lines2 = file2.readlines()  # Read all lines from the second file

        for line1, line2 in zip(lines1, lines2):  # Iterate over corresponding lines in both files
            output_file.write(f"{line1.strip()}, {line2}")  # Write zipped lines to the output file


zip_files('Goldie2019JulyFiltered.csv', 'MLRC2019JulyFiltered.csv', 'GoldieMLRCJuly.csv')  # Zip files together
