import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")

csv_files = list(raw_folder.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 80)
    print(f"File: {file.name}")

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")

    print("\n")