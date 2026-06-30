import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# -------------------------------
# Convert transaction date
# -------------------------------
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# -------------------------------
# Standardize transaction type
# -------------------------------
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

# -------------------------------
# Remove invalid amount
# -------------------------------
df = df[df["amount_inr"] > 0]

# -------------------------------
# Standardize KYC status
# -------------------------------
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

valid_status = ["Verified", "Pending", "Rejected"]

print("\nUnique KYC Status:")
print(df["kyc_status"].unique())

invalid = df[~df["kyc_status"].isin(valid_status)]

print("\nInvalid KYC Records:", len(invalid))

# -------------------------------
# Remove duplicates
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# Save cleaned file
# -------------------------------
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\nTransactions cleaned successfully.")
print("Final Shape:", df.shape)