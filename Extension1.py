"""
Name of File: extension1.py
Date: 09/20/2023
Author's Name: Aikins Acheampong

Purpose: This project involves processing and analyzing temperature data from two CSV files for the months of July and August, comparing their maximum, minimum, and average temperatures.

"""

def clearfile(filename):
    """
    Clears the content of the specified file.
    """
    fp = open(filename, 'w')  # Open the file in write mode
    fp.close()  # Close the file


gold19 = open('Goldie2019.csv', 'r')  # Open Goldie2019.csv in read mode
new_csv = ""  # Initialize an empty string to store new CSV data
lines_of_text = gold19.readlines()  # Read all lines from Goldie2019.csv

for line in lines_of_text[2:3]:  # Iterate over a slice of lines (2nd line only)
    new_csv += line  # Append the line to new_csv

size = len(lines_of_text)  # Get the total number of lines in the file

for i in range(size - 4):  # Iterate through the lines (excluding the last 2)
    line = lines_of_text[i].split(",")  # Split the line into a list of values
    mm_dd_yyyy = line[0].split('/')  # Split date into [mm, dd, yyyy]

    if mm_dd_yyyy[0] == '08':  # Check if the month is '08'
        new_csv += lines_of_text[i]  # Append the line to new_csv

clearfile('Goldie2019August.csv')  # Clear content of Goldie2019August.csv

with open("Goldie2019August.csv", "w") as new_file:  # Open Goldie2019August.csv in write mode
    new_file.write(new_csv)  # Write new_csv content to the file


mlrc19 = open('MLRCWeather2019.csv', 'r')  # Open MLRCWeather2019.csv in read mode
new_csv = ""  # Initialize an empty string to store new CSV data
lines_of_text = mlrc19.readlines()  # Read all lines from MLRCWeather2019.csv

for line in lines_of_text[:1]:  # Iterate over the first line only
    new_csv += line  # Append the line to new_csv

size = len(lines_of_text)  # Get the total number of lines in the file

for i in range(size - 2):  # Iterate through the lines (excluding the last line)
    line = lines_of_text[i].split(",")  # Split the line into a list of values
    mm_dd_yyyy = line[0].split('/')  # Split date into [mm, dd, yyyy]

    if mm_dd_yyyy[0] == '08':  # Check if the month is '08'
        new_csv += lines_of_text[i]  # Append the line to new_csv

clearfile('MLRC2019August.csv')  # Clear content of MLRC2019August.csv

new_file = open("MLRC2019August.csv", "w")  # Open MLRC2019August.csv in write mode
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



extract_columns('Goldie2019August.csv', 'Goldie2019AugustFiltered.csv', [0, 11, 16, 17, 21])  # Extract columns from Goldie2019August.csv
extract_columns('MLRC2019August.csv', 'MLRC2019AugustFiltered.csv', [2, 5, 7])  # Extract columns from MLRC2019July.csv


def zip_files(file1, file2, output_filename):
    """
    Zips the content of two files together and writes to an output file.
    """
    with open(file1, 'r') as file1, open(file2, 'r') as file2, open(output_filename, 'w') as output_file:
        lines1 = file1.readlines()  # Read all lines from the first file
        lines2 = file2.readlines()  # Read all lines from the second file

        for line1, line2 in zip(lines1, lines2):  # Iterate over corresponding lines in both files
            output_file.write(f"{line1.strip()}, {line2}")  # Write zipped lines to the output file


zip_files('Goldie2019AugustFiltered.csv', 'MLRC2019AugustFiltered.csv', 'GoldieMLRCAugust.csv')  # Zip files together








def compare_statistics(july_file, august_file):
    """
    Compare temperature statistics between two months.

    Prints the maximum, minimum, and average temperatures for both July and August.

    """

    # Open and read the July and August files
    with open(july_file, 'r') as july_fp, open(august_file, 'r') as august_fp:
        july_line = july_fp.readline()  # Read all lines in July file but skip header
        august_line = august_fp.readline() # Read all lines in  August file but skip header
        august_temps = []
        july_temps = []

        # Extract temperatures from the lines
        for july_line in july_fp:
            july_values = july_line.split(',')
            july_temps.append(float(july_values[5]))

        for august_line in august_fp:
            august_values = august_line.split(',')
            august_temps.append(float(august_values[5]))

        # Calculate statistics for July
        july_max_temp = max(july_temps)
        july_min_temp = min(july_temps)
        july_avg_temp = sum(july_temps) / len(july_temps)

        # Calculate statistics for August
        august_max_temp = max(august_temps)
        august_min_temp = min(august_temps)
        august_avg_temp = sum(august_temps) / len(august_temps)

    # Print the statistics
    print(f"July Statistics:")
    print(f"Max Temperature: {july_max_temp}")
    print(f"Min Temperature: {july_min_temp}")
    print(f"Avg Temperature: {july_avg_temp}")

    print(f"\nAugust Statistics:")
    print(f"Max Temperature: {august_max_temp}")
    print(f"Min Temperature: {august_min_temp}")
    print(f"Avg Temperature: {august_avg_temp}")

# Example usage:
compare_statistics('GoldieMLRCJuly.csv', 'GoldieMLRCAugust.csv')
