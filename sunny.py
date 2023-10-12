"""
Name of File: sunny.py
Date: 09/20/2023
Author's Name: Aikins Acheampong

Purpose: this program calculates the number of sunny and cloudy days, and the average PAR value for sunny and cloudy days.

"""
fp = open('GoldieMLRCJuly.csv', 'r')  # Open the file 'GoldieMLRCJuly.csv' in read mode
line = fp.readline()  # Read the first line from the file
numSunny = 0  # Initialize the count of sunny days to 0
numCloudy = 0  # Initialize the count of cloudy days to 0
sumSunnyPAR = 0  # Initialize the sum of PAR values on sunny days to 0
sumCloudyPAR = 0  # Initialize the sum of PAR values on cloudy days to 0
    
for line in fp:  # Iterate through the lines in the file
    values = line.split(',')  # Split the line into a list of values
    date_time = values[0]  # Extract the date and time
    time = "12:03:00 PM"  # Define a specific time
    
    if time in date_time:  # Check if the specific time matches the time in the data
        par_value = float(values[4])  # Convert PAR value to float
        
        if par_value > 800:  # Check if PAR value indicates a sunny day
            numSunny += 1  # Increment the count of sunny days
            sumSunnyPAR += par_value  # Add PAR value to the sum for sunny days
        else:
            numCloudy += 1  # Increment the count of cloudy days
            sumCloudyPAR += par_value  # Add PAR value to the sum for cloudy days


# Calculate average PAR value on sunny days
if numSunny > 0:
    avgSunnyPAR = sumSunnyPAR / numSunny 
else:
    avgSunnyPAR = 0

# Calculate average PAR value on cloudy days
if numCloudy > 0:
    avgCloudyPAR = sumCloudyPAR / numCloudy
else:
    avgCloudyPAR = 0

# Print out the results
print(f"Number of Sunny Days: {numSunny}")
print(f"Average PAR Value on Sunny Days: {avgSunnyPAR:.2f}")
print(f"Number of Cloudy Days: {numCloudy}")
print(f"Average PAR Value on Cloudy Days: {avgCloudyPAR:.2f}")

fp.close()  # Close the file
