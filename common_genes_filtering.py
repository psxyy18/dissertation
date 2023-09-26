import pandas as pd

# Specify file paths (change these to match your file locations)
jaxa_file_path = "rawcountsdataJAXA.xlsx"
gse_file_path = "output_file2.txt"

# Read the JAXA data
jaxa_data = pd.read_excel(jaxa_file_path)
# Transpose the DataFrame so genes are columns
jaxa_data = jaxa_data.transpose()
# As the first row now contains the gene names, we make it the header
jaxa_data.columns = jaxa_data.iloc[0]
jaxa_data = jaxa_data[1:]

# Load GSE data
gse_data = pd.read_csv(gse_file_path, sep='\t')

# Store the labels (assuming labels are in the first column)
labels = gse_data.iloc[:, 0]

# Extract gene names from the column headers of the GSE data, starting from the second column
gse_data.columns = gse_data.columns.str.split('|').str[2]

# Add the labels back into the dataframe
gse_data['labels'] = labels

# Compare the gene lists (columns) of the two datasets
jaxa_genes = set(jaxa_data.columns)
gse_genes = set(gse_data.columns) - {'labels'}  # excluding the 'labels' column
common_genes = jaxa_genes.intersection(gse_genes)

print("\nNumber of common genes:", len(common_genes))

# Keep only the common genes in both datasets:
jaxa_data_common = jaxa_data[list(common_genes)]
gse_data_common = gse_data[['labels'] + list(common_genes)]  # Include the 'labels' column

# Check the first few rows of the new DataFrames
print("\nJAXA data with common genes only:")
print(jaxa_data_common.head())
print("\nGSE data with common genes only:")
print(gse_data_common.head())

# Save the modified dataframes to new CSV files
jaxa_data_common.to_csv('jaxa_filtered.csv')
gse_data_common.to_csv('gse_filtered.csv')
