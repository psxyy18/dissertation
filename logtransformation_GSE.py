import numpy as np
import pandas as pd
# Load the datasets
jaxa_filtered = pd.read_csv('jaxa_filtered.csv', index_col=0)
gse_filtered = pd.read_csv('gse_filtered.csv', index_col=0)


# Remove the "labels" row from gse dataset
gse_filtered_cleaned = gse_filtered.drop('labels')

# Apply the log-transformation to the cleaned GSE dataset
gse_transformed_cleaned = gse_filtered_cleaned.applymap(lambda x: np.log2(float(x) + 1))
jaxa_transformed_cleaned = jaxa_filtered.applymap(lambda x: np.log2(float(x) + 1))

# Checking for any non-numeric values in the transformed GSE dataset
non_numeric_gse_cleaned = gse_transformed_cleaned.applymap(np.isreal).all().all()
non_numeric_jaxa_cleaned = jaxa_transformed_cleaned.applymap(np.isreal).all().all()
print(non_numeric_jaxa_cleaned)
print(non_numeric_gse_cleaned)
# Save the cleaned and transformed GSE, jaxa dataset
gse_transformed_cleaned_path = 'gse_logtransformed_cleaned.csv'
gse_transformed_cleaned.to_csv(gse_transformed_cleaned_path)
jaxa_transformed_cleaned_path = 'jaxa_logtransformed_cleaned.csv'
jaxa_transformed_cleaned.to_csv(jaxa_transformed_cleaned_path)