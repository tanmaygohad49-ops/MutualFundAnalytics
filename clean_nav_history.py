import pandas as pd

# Read data
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and date
df = df.sort_values(["amfi_code", "date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Forward-fill missing NAV values within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Keep only valid NAV values
df = df[df["nav"] > 0]

# Save cleaned data
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("NAV History cleaned successfully.")
print(df.shape)