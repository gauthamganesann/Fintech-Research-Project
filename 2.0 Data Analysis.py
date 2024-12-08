# Fintech Research Project
# Data Analysis

# Steps,
# 1. Import the clean data
# 2. Rename the columns
# 3. Filter the relevant columns
# 4. Set the Date column as index
# 5. Check for the data type of closing prices to be numeric
# 6. Calculate the daily returns
# 7. Combine the daily returns into a single dataframe based on overlapping dates
# 8. Calculate the rolling correlations
# 9. Export the result


import pandas as pd


# Step 1: Imports the clean data
sp_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/S&P clean data.xlsx"
nas_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/Nasdaq clean data.xlsx"
btc_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/BTC USD clean data.xlsx"
eth_clean_filepath = "/Users/gauthamganesan/Downloads/Fintech/3 Clean Data/ETH USD clean data.xlsx"

sp_data = pd.read_excel(sp_clean_filepath, parse_dates=["Date"])
nas_data = pd.read_excel(nas_clean_filepath, parse_dates=["Date"])
btc_data = pd.read_excel(btc_clean_filepath, parse_dates=["Date"])
eth_data = pd.read_excel(eth_clean_filepath, parse_dates=["Date"])


# Step 2: Renames the columns
sp_data.columns = ["Date", "SP_Adj_Close", "SP_Volume"]
nas_data.columns = ["Date", "Nasdaq_Adj_Close", "Nasdaq_Volume"]
btc_data.columns = ["Date", "BTC_USD_Close", "Volume_BTC", "Volume_USD"]
eth_data.columns = ["Date", "ETH_USD_Close", "Volume_ETH", "Volume_USD"]



# Step 3: Filters the relevant columns
sp_data = sp_data.iloc[:, 0:2]
nas_data = nas_data.iloc[:, 0:2]
btc_data = btc_data.iloc[:, 0:2]
eth_data = eth_data.iloc[:, 0:2]


# Step 4: Sets the Date column as index
btc_data["Date"] = btc_data["Date"].dt.floor("D")  # Removes time component
eth_data["Date"] = eth_data["Date"].dt.floor("D")  # Removes time component

sp_data.set_index("Date", inplace=True)
nas_data.set_index("Date", inplace=True)
btc_data.set_index("Date", inplace=True)
eth_data.set_index("Date", inplace=True)


# Step 5: Checks for the data type of closing prices to be numeric
sp_data["SP_Adj_Close"] = pd.to_numeric(sp_data["SP_Adj_Close"], errors="coerce")
nas_data["Nasdaq_Adj_Close"] = pd.to_numeric(nas_data["Nasdaq_Adj_Close"], errors="coerce")
btc_data["BTC_USD_Close"] = pd.to_numeric(btc_data["BTC_USD_Close"], errors="coerce")
eth_data["ETH_USD_Close"] = pd.to_numeric(eth_data["ETH_USD_Close"], errors="coerce")


# Step 6: Calculates the daily returns
sp_data["SP_Return"] = sp_data["SP_Adj_Close"].pct_change()
nas_data["Nasdaq_Return"] = nas_data["Nasdaq_Adj_Close"].pct_change()
btc_data["BTC_Return"] = btc_data["BTC_USD_Close"].pct_change()
eth_data["ETH_Return"] = eth_data["ETH_USD_Close"].pct_change()


# Step 7: Combine the daily returns into a single dataframe based on overlapping dates
combined_data = sp_data[["SP_Return"]].join(
    nas_data[["Nasdaq_Return"]],
    how="inner"
).join(
    btc_data[["BTC_Return"]],
    how="inner"
).join(
    eth_data[["ETH_Return"]],
    how="inner"
)


# Step 8: Calculates the rolling correlations
# Using a 30-day rolling window
window_size = 30

combined_data["BTC_SP_Corr"] = combined_data["BTC_Return"].rolling(window=window_size).corr(combined_data["SP_Return"])
combined_data["ETH_SP_Corr"] = combined_data["ETH_Return"].rolling(window=window_size).corr(combined_data["SP_Return"])
combined_data["BTC_Nasdaq_Corr"] = combined_data["BTC_Return"].rolling(window=window_size).corr(combined_data["Nasdaq_Return"])
combined_data["ETH_Nasdaq_Corr"] = combined_data["ETH_Return"].rolling(window=window_size).corr(combined_data["Nasdaq_Return"])


# Step 9: Exports the result
result_excel_filepath = "/Users/gauthamganesan/Downloads/Fintech/5 Fintech Data Analysis.xlsx"
result_csv_filepath = "/Users/gauthamganesan/Downloads/Fintech/5 Fintech Data Analysis.csv"

combined_data.to_excel(result_excel_filepath)
combined_data.to_csv(result_csv_filepath)
