import pandas as pd
import numpy as np

# Load the JAXA dataset
jaxa_df = pd.read_csv("jaxa_filtered.csv", index_col=0)

# Define conditions
conditions = ["Pre - Means", "Flight - Means", "Post - Means"]

# Extract rows for each condition
preflight_data = jaxa_df.loc[conditions[0]].to_frame()
inflight_data = jaxa_df.loc[conditions[1]].to_frame()
postflight_data = jaxa_df.loc[conditions[2]].to_frame()

# Rename the columns for clarity
preflight_data.columns = ["Preflight_Mean_Counts"]
inflight_data.columns = ["Inflight_Mean_Counts"]
postflight_data.columns = ["Postflight_Mean_Counts"]

# Combine the datasets horizontally
combined_data = pd.concat([preflight_data, inflight_data, postflight_data], axis=1)

# Round the values for the entire DataFrame
combined_data_rounded = combined_data.round()

# Convert to integers
combined_data_int = combined_data_rounded.astype(int)

# Filter out rows with all zero counts across the conditions
non_zero_rows = (combined_data_int != 0).any(axis=1)
combined_data_filtered = combined_data_int[non_zero_rows]

# Check the values
print(combined_data_filtered.head())

# Save the combined data to a CSV file
combined_data_filtered.to_csv("combined_processed.csv", index=True)

