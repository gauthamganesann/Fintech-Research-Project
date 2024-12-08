# Fintech Research Project
# Data Collection

# Steps,
# 1. Establised the required tickers, start and end date
# 2. Download the data from yahoo finance
# 3. Export the raw data


import pandas as pd
import yfinance as yf


# Step 1: Establishes the required tickers, start and end date
tickers = {
    "S&P_500": "^GSPC",
    "Nasdaq": "^IXIC"
}
start_date = "2020-01-06"
end_date = "2022-12-01"
result = {}


# Step 2: Downloads the data from yahoo finance
for (name, ticker) in tickers.items():
    data = yf.download(ticker, start=start_date, end=end_date)
    result[name] = data


# Step 3: Exports the raw data
sp_raw_filepath = "/Users/gauthamganesan/Downloads/Fintech/2 Raw Data/S&P raw data.csv"
nasdaq_raw_filepath = "/Users/gauthamganesan/Downloads/Fintech/2 Raw Data/Nasdaq raw data.csv"

for name, df in result.items():
    if name=="S&P_500":
        df.to_csv(sp_raw_filepath)
    if name=="Nasdaq":
        df.to_csv(nasdaq_raw_filepath)
