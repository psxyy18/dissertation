import pandas as pd
# Load the cleaned GSE dataset with low_memory=False to avoid DtypeWarning
gse_logtransformed = pd.read_csv('gse_logtransformed_cleaned.csv', index_col=0, low_memory=False)
jaxa_logtransformed = pd.read_csv('jaxa_logtransformed_cleaned.csv', index_col=0, low_memory=False)

# Store labels from GSE for later use
gse_labels = gse_logtransformed.iloc[0]
gse_logtransformed = gse_logtransformed.drop('labels')  # Remove the "labels" row

# Transpose JAXA dataset as its genes are columns
jaxa_logtransformed = jaxa_logtransformed.transpose()

# Convert GSE dataset values to numeric
gse_logtransformed = gse_logtransformed.apply(pd.to_numeric, errors='coerce')

# Ensure only numeric columns are considered for GSE
numeric_columns_gse = gse_logtransformed.select_dtypes(include=['number']).columns

# Calculate mean and standard deviation for numeric columns for GSE
mean_gse_new = gse_logtransformed[numeric_columns_gse].mean(axis=1)
std_gse_new = gse_logtransformed[numeric_columns_gse].std(axis=1)

# Filter genes based on the criteria for GSE
filtered_genes_gse_new = gse_logtransformed.index[(mean_gse_new >= 0.8) & (std_gse_new >= 0.8)]
filtered_gse_logtransformed_new = gse_logtransformed.loc[filtered_genes_gse_new]

# Convert JAXA dataset values to numeric
jaxa_logtransformed = jaxa_logtransformed.apply(pd.to_numeric, errors='coerce')

# Ensure only numeric columns are considered for JAXA
numeric_columns_jaxa = jaxa_logtransformed.select_dtypes(include=['number']).columns

# Calculate mean and standard deviation for numeric columns for JAXA
mean_jaxa = jaxa_logtransformed[numeric_columns_jaxa].mean(axis=1)
std_jaxa = jaxa_logtransformed[numeric_columns_jaxa].std(axis=1)

# Filter genes based on the criteria for JAXA
filtered_genes_jaxa = jaxa_logtransformed.index[(mean_jaxa >= 0.8) & (std_jaxa >= 0.8)]
filtered_jaxa_logtransformed = jaxa_logtransformed.loc[filtered_genes_jaxa]

# Determine common genes
common_genes = list(set(filtered_genes_gse_new).intersection(set(filtered_genes_jaxa)))

# Filter datasets to include only common genes
common_gse = filtered_gse_logtransformed_new.loc[common_genes]
common_jaxa = filtered_jaxa_logtransformed.loc[common_genes]

# Add back the labels row to the GSE dataset
common_gse.loc['labels'] = gse_labels

# Save the resulting datasets to new CSV files
common_gse.to_csv('common_genes_gse.csv')
common_jaxa.to_csv('common_genes_jaxa.csv')

print(len(filtered_genes_gse_new), len(filtered_genes_jaxa), len(common_genes))
