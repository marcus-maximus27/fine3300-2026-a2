'''
InflationCalculator.py

FINE 3300 (Fall 2026): Assignment #2
Author: Marcus Maximus Reyes

Description:
    Reads monthly Consumer Price Index (CPI) data from the Bank of Canada,
    graphs the CPI and its annual percentage change, and calculates the
    effect of inflation on a price between two months.

Sources:
    - FINE 3300 Lectures 6 to 8 class examples (Pandas, Matplotlib, NumPy)
    - Bank of Canada Inflation Calculator: https://www.bankofcanada.ca/rates/related/inflation-calculator/
    - pandas read_csv documentation (skiprows): https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
'''

# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Part 1: Clean the data

# skip the first 8 rows of the CSV file and read the data into a pandas DataFrame
data = pd.read_csv('STATIC_INFLATIONCALC.csv', skiprows=8)

# rename columns for clarity
data = data.rename(columns={'date': 'Date', 'STATIC_INFLATIONCALC': 'CPI'})

# convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# filter the data to only include the first day of each month
data = data[data['Date'].dt.day == 1]

# renumber the index of the DataFrame after filtering
data = data.reset_index(drop=True)

# calculates percentage change in CPI over a 12-month period and adds it as a new column to the DataFrame
data['Annual Percentage Change (%)'] = data['CPI'].pct_change(periods=12) * 100

# print(data.tail())

# Part 2: Graph the CPI over time
fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')

ax.plot(data['Date'], data['CPI'], color='blue', label='CPI')

ax.set_xlabel('Date')
ax.set_ylabel('CPI (2002 = 100)')
ax.set_title('Consumer Price Index (CPI) Over Time')

# Add a horizontal line at CPI = 100
ax.axhline(y=100, linestyle=':', color='gray', label='Base level (2002 = 100)')

# Add a second y-axis for the annual percentage change
ax2 = ax.twinx()
ax2.plot(data['Date'], data['Annual Percentage Change (%)'], color='orange', label='Annual Percentage Change (%)', linewidth=0.8)
ax2.set_ylabel('Annual Percentage Change (%)')

lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='lower right')

ax2.legend(lines1 + lines2, labels1 + labels2, loc='lower right')

# plt.show()

# Part 3: Inflation Calculator

'''
Enter the price          →  validate (a positive number?)
Enter the first date     →  validate format, extract year and month, check it's in the data
Enter the second date    →  same checks
Look up both CPIs        →  filter cpi_data by year and month
Calculate                →  new price, % change, years, annual rate
Print results            →  $, 2 decimals, CAD, like the BoC page

'''

# Function to get a valid price input from the user
def get_price():

    while True:
        entry = input("Enter the price: ")
        entry = entry.replace('$', '').replace(',', '')  # Remove commas and dollar signs from the input
        try:
            price = float(entry)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if price <= 0:
            print("Invalid input. Please enter a positive number.")
            continue

        return price

# Function to get a valid date input from the user
def get_date(prompt):
    while True:
        entry = input(prompt).strip() # Remove leading and trailing whitespace
        try:
            date = pd.to_datetime(entry, format='%Y-%m')
        except ValueError:
            print("Invalid input. Please enter a date in the format YYYY-MM.")
            continue

        if date not in data['Date'].values:
            earliest = data['Date'].min().strftime('%Y-%m')
            latest = data['Date'].max().strftime('%Y-%m')
            print("Please enter a date between {} and {}.".format(earliest, latest))
            continue

        return date

# Function to get the CPI for a given date
def get_cpi(date):
    row = data[(data['Date'].dt.year == date.year) & (data['Date'].dt.month == date.month)]
    return row['CPI'].values[0]

# Main program: get user inputs
price = get_price()
first_date = get_date("Enter the first date (YYYY-MM): ")
second_date = get_date("Enter the second date (YYYY-MM): ")

cpi_1 = get_cpi(first_date)
cpi_2 = get_cpi(second_date)

# Calculations
new_price = price * (cpi_2 / cpi_1)
percent_change = (new_price - price) / price * 100
no_months = (second_date.year - first_date.year) * 12 + (second_date.month - first_date.month)
no_years = no_months / 12

if no_months == 0:
    avg_annual_rate = 0
else:
    avg_annual_rate = (np.power((cpi_2 / cpi_1), (1 / no_years)) - 1) * 100

# Return values
# print(first_date.year, first_date.month, get_cpi(first_date))
# print(second_date.year, second_date.month, get_cpi(second_date))

print(new_price, percent_change, no_months, no_years, avg_annual_rate)

