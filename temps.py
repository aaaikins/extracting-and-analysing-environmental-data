"""
Name of File: temps.py
Date: 09/20/2023
Author's Name: Aikins Acheampong

Purpose: this program computes the high and low air temperature and the water temperature at 3 meters depth.

"""



fp = open('GoldieMLRCJuly.csv', 'r')  # Open the file 'GoldieMLRCJuly.csv' in read mode
line = fp.readline()  # Read the first line from the file

high_air_temp = -200  # Initialize the highest air temperature to a very low value
low_air_temp = 10000000  # Initialize the lowest air temperature to a very high value
high_water_temp = -200  # Initialize the highest water temperature to a very low value
low_water_temp = 1000000  # Initialize the lowest water temperature to a very high value
    
for line in fp:  # Iterate through the lines in the file
    values = line.split(',')  # Split the line into a list of values
    air_temp = float(values[5])  # Convert air temperature to float
    date = values[0]  # Extract the date
    water_temp = float(values[1])  # Convert water temperature to float

    if air_temp > high_air_temp:  # Check if current air temperature is higher than highest recorded
        high_air_temp = air_temp  # Update highest air temperature
        high_date = date  # Update date for highest air temperature
    elif air_temp < low_air_temp:  # Check if current air temperature is lower than lowest recorded
        low_air_temp = air_temp  # Update lowest air temperature
        low_date = date  # Update date for lowest air temperature

    if water_temp > high_water_temp:  # Check if current water temperature is higher than highest recorded
        high_water_temp = water_temp  # Update highest water temperature
        high_water_date = date  # Update date for highest water temperature
    elif water_temp < low_water_temp:  # Check if current water temperature is lower than lowest recorded
        low_water_temp = water_temp  # Update lowest water temperature
        low_water_date = date  # Update date for lowest water temperature

# print out the results
print(f"Highest Air Temperature: {high_air_temp} °C Occurs on {high_date}")  # Print highest air temperature and date
print(f"Lowest Air Temperature: {low_air_temp} °C Occurs on {low_date}")  # Print lowest air temperature and date
print(f"Highest Water Temperature at 3 meters: {high_water_temp} °C Occurs on {high_water_date}")  # Print highest water temperature and date
print(f"Lowest Water Temperature at 3 meters: {low_water_temp} °C Occurs on {low_water_date}")  # Print lowest water temperature and date

fp.close()  # Close the file
