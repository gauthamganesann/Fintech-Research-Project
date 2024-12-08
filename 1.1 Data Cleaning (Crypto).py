# Fintech Research Project
# Data Cleaning (Crypto)

# Steps:
# 1. Import the raw data
# 2. Rename the columns
# 3. Convert the Date column into a datetime object
# 4. Set the Date column as the index
# 5. Sort the dates in ascending order
# 6. Filter the data for the required timeframe
# 7. Check for missing values
# 8. Filter and retain the relevant columns
#    Retain: Close Price, Volume BTC/ETH, Volume USD
# 9. Export the clean data


import pandas as pd


# Step 1: Imports the raw data
btc_raw_filepath = "/Users/gauthamganesan/Downloads/Fintech/2 Raw Data/BTC USD raw data.csv"
eth_raw_filepath = "/Users/gauthamganesan/Downloads/Fintech/2 Raw Data/ETH USD raw data.csv"

btc_data = pd.read_csv(btc_raw_filepath)
eth_data = pd.read_csv(eth_raw_filepath)


# Step 2: Renames the columns
btc_data.columns = ["Timestamp", "Date", "Symbol", "Open Price", "High Price", "Low Price", "Close Price", "Volume BTC", "Volume USD"]
eth_data.columns = ["Timestamp", "Date", "Symbol", "Open Price", "High Price", "Low Price", "Close Price", "Volume ETH", "Volume USD"]


# Step 3: Converts the Date column into a datetime object
btc_data["Date"] = pd.to_datetime(btc_data["Date"], format="%d/%m/%Y %H:%M", errors="coerce")
eth_data["Date"] = pd.to_datetime(eth_data["Date"], format="%d/%m/%Y %H:%M", errors="coerce")



# Step 4: Sets the Date column as the index
btc_data.set_index("Date", inplace=True)
eth_data.set_index("Date", inplace=True)


# Step 5: Sorts the dates in ascending order
btc_data.sort_index(inplace=True)
eth_data.sort_index(inplace=True)


# Step 6: Filters the data for the required timeframe
start_date = "2020-01-06"
end_date = "2022-12-01"

btc_data = btc_data.loc[start_date:end_date]
eth_data = eth_data.loc[start_date:end_date]


# Step 7: Checks for missing values
print("Missing values in Bitcoin data:")
print(btc_data.isnull().sum())  # Check for missing values in Bitcoin data
print("\nMissing values in Ethereum data:")
print(eth_data.isnull().sum())  # Check for missing values in Ethereum data


# Step 8: Filters and retains the relevant columns
btc_data = btc_data[["Close Price", "Volume BTC", "Volume USD"]]
eth_data = eth_data[["Close Price", "Volume ETH", "Volume USD"]]

print("Bitcoin Data (First 5 Rows):")
print(btc_data.head())
print("\nEthereum Data (First 5 Rows):")
print(eth_data.head())


# Step 9: Exports the clean data
btc_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/BTC USD clean data.csv"
eth_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/ETH USD clean data.csv"

btc_data.to_csv(btc_clean_filepath, index=True)
eth_data.to_csv(eth_clean_filepath, index=True)
