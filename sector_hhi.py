import pandas as pd

# Load portfolio holdings
portfolio = pd.read_csv("data/processed/portfolio_holdings_cleaned.csv")

# Total holding per sector
sector = (
    portfolio.groupby("sector")["weight_pct"]
    .sum()
    .reset_index()
)

# Convert to proportion
sector["share"] = sector["weight_pct"] / sector["weight_pct"].sum()

# HHI
hhi = (sector["share"] ** 2).sum()

print(f"Sector HHI: {hhi:.4f}")

# Save report
sector.to_csv("reports/sector_hhi.csv", index=False)

print("Saved to reports/sector_hhi.csv")