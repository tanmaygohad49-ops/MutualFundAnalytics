# Data Quality Summary

## Fund Master
- Total AMFI Codes: 40
- Missing AMFI Codes: 0

## NAV History
- Total NAV Codes: 40
- Missing Values: Check using data_ingestion.py
- Duplicate Rows: Check using data_ingestion.py

## Overall
- Number of datasets: 10
- Data issues identified:
  - No AMFI code mismatch found.
- Recommendations:
  - Convert date columns to datetime.
  - Verify missing values before analysis.
  - Remove duplicate rows if any are found.