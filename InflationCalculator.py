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

print(data.tail())

# part 1: Graph the CPI over time
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

plt.show()



