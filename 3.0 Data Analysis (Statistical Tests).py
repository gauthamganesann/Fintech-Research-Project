# Fintech Research Project
# Hypothesis Testing on Rolling Correlation Data

# Steps:
# 1. Import the rolling correlation data.
# 2. Define market cycles and rolling correlation columns to test.
# 3. Perform hypothesis tests (H1 and H2).
# 4. Export the results.

# Step 1: Import the rolling correlation data
input_file_path = '/Users/gauthamganesan/Downloads/1 Fintech Data Analysis/5 Fintech Data Analysis.xlsx'
data = pd.ExcelFile(input_file_path)
rolling_data = data.parse("Sheet1")

# Step 2: Define market cycles and rolling correlation columns to test
rolling_data['Date'] = pd.to_datetime(rolling_data['Date'])  # Convert 'Date' column to datetime format

market_cycles = {
    "Bear (COVID-19 Crash)": ("2020-02-19", "2020-03-23"),
    "Bull (Stimulus and Recovery)": ("2020-03-24", "2022-01-03"),
    "Bear (Inflation Concerns)": ("2022-01-04", "2022-10-12"),
    "Bull (Temporary Recovery)": ("2022-10-13", "2022-12-01"),
}

columns_to_test = ['BTC_SP_Corr', 'ETH_SP_Corr', 'BTC_Nasdaq_Corr', 'ETH_Nasdaq_Corr']

# Step 3: Perform hypothesis tests (H1 and H2)
results = {}

# Perform pairwise t-tests for mean comparisons (H1)
for column in columns_to_test:
    cycle_data = {cycle: rolling_data[(rolling_data['Date'] >= start) & (rolling_data['Date'] <= end)][column].dropna()
                  for cycle, (start, end) in market_cycles.items()}

    bull_data = pd.concat([cycle_data[cycle] for cycle in market_cycles if "Bull" in cycle])
    bear_data = pd.concat([cycle_data[cycle] for cycle in market_cycles if "Bear" in cycle])
    t_stat_h1, p_value_h1 = stats.ttest_ind(bull_data, bear_data, equal_var=False, alternative='greater')

    results[column] = {
        "H1_t-statistic": t_stat_h1,
        "H1_p-value": p_value_h1
    }

# Perform F-test for variance comparisons (H2)
for column in columns_to_test:
    bull_data = pd.concat([rolling_data[(rolling_data['Date'] >= start) & (rolling_data['Date'] <= end)][column].dropna()
                           for cycle, (start, end) in market_cycles.items() if "Bull" in cycle])
    bear_data = pd.concat([rolling_data[(rolling_data['Date'] >= start) & (rolling_data['Date'] <= end)][column].dropna()
                           for cycle, (start, end) in market_cycles.items() if "Bear" in cycle])

    f_stat_h2 = bull_data.var() / bear_data.var()
    p_value_h2 = stats.f.cdf(f_stat_h2, dfn=len(bull_data) - 1, dfd=len(bear_data) - 1)

    results[column]["H2_f-statistic"] = f_stat_h2
    results[column]["H2_p-value"] = p_value_h2

# Step 4: Export the results
output_file_path = '/Users/gauthamganesan/Downloads/1 Fintech Data Analysis/6 Fintech Hypothesis Tests.xlsx'

output_data = []
for column, metrics in results.items():
    output_data.append({"Rolling Correlation": column, **metrics})

output_df = pd.DataFrame(output_data)
output_df.to_excel(output_file_path, index=False)
