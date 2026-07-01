import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Files to copy
files = {
    "01_fund_master.csv": "fund_master_cleaned.csv",
    "03_aum_by_fund_house.csv": "aum_by_fund_house_cleaned.csv",
    "04_monthly_sip_inflows.csv": "monthly_sip_inflows_cleaned.csv",
    "05_category_inflows.csv": "category_inflows_cleaned.csv",
    "06_industry_folio_count.csv": "industry_folio_count_cleaned.csv",
    "09_portfolio_holdings.csv": "portfolio_holdings_cleaned.csv",
    "10_benchmark_indices.csv": "benchmark_indices_cleaned.csv"
}

for input_file, output_file in files.items():

    path = os.path.join("data", "raw", input_file)

    df = pd.read_csv(path)

    output_path = os.path.join("data", "processed", output_file)

    df.to_csv(output_path, index=False)

    print(f"✔ {output_file} created ({len(df)} rows)")

print("\n🎉 All remaining processed CSVs created successfully!")