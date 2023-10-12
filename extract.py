"""
Name of File: extract.py
Date: 09/20/2023
Author's Name: Aikins Acheampong

Purpose: this program extracts the air temperature at 3:03pm on each day of July and writes it in a CSV file(airTemp_3m.csv)

"""


# open the GoldieMLRCJuly.csv file
with open('GoldieMLRCJuly.csv', 'r') as fp:
    line = fp.readline()
    # initialize variables
    extracted_data = []


    # iterate through each line in the file
    for line in fp:
        # split the line into a list of values
        values = line.split(',')

        # extract date/time field
        date_time = values[0]

        # assign "3:03:00PM" to time
        time = "3:03:00 PM"
        
        # check if the time is "3:03:00 PM"
        if time in date_time:

            # extract day of the month and air temperature
            day = int(values[0].split('/')[1])
            air_temp_3pm = float(values[5])

            # append to extracted data
            extracted_data.append((day, air_temp_3pm))

# write to CSV file
with open('extracted_data.csv', 'w') as out_fp:
    out_fp.write("Day,3pmTemp\n")
    for day, temp in extracted_data:
        out_fp.write(f"{day},{temp}\n")
