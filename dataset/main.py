import pandas as pd
from datasets import load_dataset

# Load the dataset
ds = load_dataset("patriziobellan/PET", "relations-extraction")

# Convert the test split to a pandas DataFrame
df_test = ds['test'].to_pandas()

# Write the DataFrame to a CSV file
csv_filename = "relations_extraction_test.csv"
df_test.to_csv(csv_filename, index=False)

print(f"Dataset written to {csv_filename}")
