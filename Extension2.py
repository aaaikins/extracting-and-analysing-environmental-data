"""
Name of File: Extension2.py
Date: 09/20/2023
Author's Name: Aikins Acheampong

Purpose: this program calculates the average air temperature per day for July.

"""



def average_air_temp_per_day(file, month):
    with open(file, 'r') as fp:
        line = fp.readline()[1:]  # Skip header

        daily_values = {}

        # Extract and accumulate air temperatures for each day of the month
        for line in fp:
            values = line.split(',')
            day = int(values[0].split('/')[1])
            air_temp = float(values[5])  # Assuming air temperature is in column 11

            if day not in daily_values:
                daily_values[day] = []

            daily_values[day].append(air_temp)

        # Calculate average air temperature for each day
        for day, temps in daily_values.items():
            avg_temp = sum(temps) / len(temps)
            print(f"Day {day} of {month}: Average Air Temperature = {avg_temp:.2f} °C")

# Example usage:
average_air_temp_per_day('GoldieMLRCJuly.csv', 'July')
average_air_temp_per_day('GoldieMLRCAugust.csv', 'August')
