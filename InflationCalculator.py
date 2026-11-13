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
cpi_data = pd.read_csv('STATIC_INFLATIONCALC.csv', skiprows=8)

# rename columns for clarity
cpi_data = cpi_data.rename(columns={'date': 'Date', 'STATIC_INFLATIONCALC': 'CPI'})

print(cpi_data.head(1))
print(100 * '-')
print(cpi_data.tail(1))
print(100 * '-')
cpi_data.info()
print(100 * '-')