import pandas as pd

# Load data
funds = pd.read_csv("data/processed/scheme_performance_cleaned.csv")

# Remove extra spaces
funds["risk_grade"] = funds["risk_grade"].astype(str).str.strip()

print("Available Risk Levels:")
print(funds["risk_grade"].unique())

# User input
risk = "Moderate"

# Filter funds
recommendation = funds[
    funds["risk_grade"].str.lower() == risk.lower()
]

# Sort by Sharpe Ratio
recommendation = recommendation.sort_values(
    by="sharpe_ratio",
    ascending=False
).head(3)

# Check result
if recommendation.empty:
    print("\nNo funds found for this risk level.")
else:
    print("\nTop 3 Recommended Funds\n")

    print(
        recommendation[
            [
                "scheme_name",
                "risk_grade",
                "sharpe_ratio",
                "morningstar_rating",
                "return_3yr_pct"
            ]
        ]
    )

    recommendation.to_csv(
        "reports/fund_recommendation.csv",
        index=False
    )

    print("\nRecommendation saved to reports/fund_recommendation.csv")