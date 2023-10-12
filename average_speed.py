"""
Name of File: average_speed.py
Date: 09/20/2023
Author's Name: Aikins Acheampong

Purpose: this program calculates the average wind speed for July.

"""


fp = open('GoldieMLRCJuly.csv', 'r')  # Open the file 'GoldieMLRCJuly.csv' in read mode
line = fp.readline()  # Read the first line from the file
total_wind_speed = 0  # Initialize the sum of wind speeds
num_entries = 0  # Initialize the count of entries

for line in fp:  # Iterate through the lines in the file
    values = line.split(',')  # Split the line into a list of values
    wind_speed = float(values[5])  # Convert wind speed to float
    total_wind_speed += wind_speed  # Add wind speed to the total
    num_entries += 1  # Increment the count of entries

# Calculate average wind speed
if num_entries > 0:
    avg_wind_speed = total_wind_speed / num_entries  
else:
    avg_wind_speed = 0

# Print out the result
print(f"Average Wind Speed for July: {avg_wind_speed:.2f} m/s")

fp.close()  # Close the file
