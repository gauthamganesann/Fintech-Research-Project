# Fintech Research Project
# Data Cleaning (Market)

# Steps,
# 1. Import the raw data
# 2. Rename the columns and removes the irrelevant rows
# 3. Convert the Date column into datetime object
# 4. Set the Date column as index
# 5. Check for missing values
# 6. Retain the relevant columns
#    Date is already the index, Adj Close Price, Volume
# 7. Export the clean data


import pandas as pd

# Step 1: Imports the raw data
sp_raw_filepath = "/Users/gauthamganesan/Downloads/Fintech/2 Raw Data/S&P raw data.csv"
nas_raw_filepath = "/Users/gauthamganesan/Downloads/Fintech/2 Raw Data/Nasdaq raw data.csv"

sp_data = pd.read_csv(sp_raw_filepath)
nas_data = pd.read_csv(nas_raw_filepath)


# Step 2: Renames the columns and removes the irrelevant rows
sp_data.columns = ["Date", "Adj Close Price", "Close Price", "High Price", "Low Price", "Open Price", "Volume"]
nas_data.columns = ["Date", "Adj Close Price", "Close Price", "High Price", "Low Price", "Open Price", "Volume"]

sp_data = sp_data.iloc[2:,:]
nas_data = nas_data.iloc[2:,:]


# Step 3: Converts the Date column into datetime format
sp_data["Date"] = pd.to_datetime(sp_data["Date"])
nas_data["Date"] = pd.to_datetime(nas_data["Date"])


# Step 4: Sets the Date column as index and converts it into YYYY-MM-DD format
sp_data.set_index("Date", inplace=True)
nas_data.set_index("Date", inplace=True)

sp_data.index = sp_data.index.strftime('%Y-%m-%d')
nas_data.index = nas_data.index.strftime('%Y-%m-%d')


# Step 5: Checks for missing values
print(sp_data.isnull().sum())
print()
print(nas_data.isnull().sum())


# Step 6: Retains the relevant columns
sp_data = sp_data[["Adj Close Price", "Volume"]]
nas_data = nas_data[["Adj Close Price", "Volume"]]


# Step 7: Exports the clean data
sp_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/S&P clean data.csv"
nas_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/Nasdaq clean data.csv"

sp_data.to_csv(sp_clean_filepath)
nas_data.to_csv(nas_clean_filepath)
