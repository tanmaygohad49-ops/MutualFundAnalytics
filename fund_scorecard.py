import pandas as pd

# Load data
funds = pd.read_csv("data/processed/scheme_performance_cleaned.csv")

# Score calculation
funds["score"] = (
    funds["sharpe_ratio"] * 0.40
    + funds["morningstar_rating"] * 0.30
    + funds["return_3yr_pct"] * 0.30
)

# Top funds
scorecard = (
    funds.sort_values("score", ascending=False)
    .reset_index(drop=True)
)

# Save
scorecard.to_csv(
    "reports/fund_scorecard.csv",
    index=False
)

print("Fund Scorecard created successfully!")
print(scorecard.head(10))