import pandas as pd

# Load the GSE dataset
gse_data = pd.read_csv("gse_filtered.csv", index_col=0)

# Transpose the GSE dataset
gse_data_transposed = gse_data.transpose()

# Save the transposed GSE data to a new CSV file
gse_data_transposed.to_csv("gse_filtered.csv", index=True)
