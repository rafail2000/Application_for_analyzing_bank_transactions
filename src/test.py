import yfinance as yf
import pandas as pd

tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Import pandas
data = pd.DataFrame(columns=tickers_list)

# Fetch the data

for ticker in tickers_list:
    data[ticker] = yf.download(ticker,'2025-01-01')

# Print first 5 rows of the data
data.head()