import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Convert return columns to numeric
# -----------------------------
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# Check for missing numeric values
# -----------------------------
print("\nMissing Values:")
print(df[return_cols].isnull().sum())

# -----------------------------
# Expense Ratio Validation
# -----------------------------
valid_expense = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nValid Expense Ratio Records :", len(valid_expense))
print("Invalid Expense Ratio Records :", len(invalid_expense))

# -----------------------------
# Find anomalies
# -----------------------------
print("\nChecking Return Columns...")

for col in [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]:
    print(f"{col}:")
    print("Minimum =", df[col].min())
    print("Maximum =", df[col].max())
    print()

# -----------------------------
# Remove duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Save cleaned data
# -----------------------------
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("✅ Scheme Performance cleaned successfully.")
print("Final Shape:", df.shape)