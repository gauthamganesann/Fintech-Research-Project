# Fintech Research Project
# Data Cleaning (Crypto)

# Steps,
# 1. Import the raw data
# 2. Rename the columns
# 3. Convert the Date column into datetime object
# 4. Set the Date column as the index and convert it into YYYY-MM-DD format
# 5. Filter the data for the required timeframe
# 6. Check for missing values
# 7. Sort the dates in ascending order (earliest to latest)
# 8. Filter and retain the relevant columns
#    Date is already the index, Close Price, Volume BTC ; Volume ETH, Volume USD
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


# Step 3: Converts the Date column into datetime object
btc_data["Date"] = pd.to_datetime(btc_data["Date"], format="%d/%m/%Y %H:%M")
eth_data["Date"] = pd.to_datetime(eth_data["Date"], format="%d/%m/%Y %H:%M")


# Step 4: Sets the Date column as the index and converts it into YYYY-MM-DD format
btc_data.set_index("Date", inplace=True)
eth_data.set_index("Date", inplace=True)

btc_data.index = btc_data.index.strftime('%Y-%m-%d')
eth_data.index = eth_data.index.strftime('%Y-%m-%d')


# Step 5: Filters the data for the required timeframe
start_date = "2020-02-19"
end_date = "2022-12-01"

btc_data = btc_data.loc[start_date:end_date]
eth_data = eth_data.loc[start_date:end_date]


# Step 6: Checks for missing values
print("Missing values in Bitcoin data:")
print(btc_data.isnull().sum())                      # btc_data.isnull() checks if the data has missing values
                                                    # returns a df containing True for missing value and False for a valid value
                                                    # btc_data.isnull().sum() counts the number of True for each column
print("\nMissing values in Ethereum data:")
print(eth_data.isnull().sum())


# Step 7: Sorts the dates in ascending order (earliest to latest)
btc_data.sort_index(inplace=True)
eth_data.sort_index(inplace=True)


# Step 8: Filters and retains the relevant columns
btc_data = btc_data[["Close Price", "Volume BTC", "Volume USD"]]
eth_data = eth_data[["Close Price", "Volume ETH", "Volume USD"]]

print(f"{eth_data.head(5)}")
print(f"\n{eth_data.tail(5)}")


# Step 9: Exports the clean data
btc_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/BTC USD clean data.csv"
eth_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/ETH USD clean data.csv"

btc_data.to_csv(btc_clean_filepath, index=True)
eth_data.to_csv(eth_clean_filepath, index=True)
