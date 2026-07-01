# Data Dictionary

## 1. fund_master

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Mutual Fund Company |
| scheme_name | Text | Scheme Name |
| category | Text | Equity/Debt/Hybrid |
| sub_category | Text | Large Cap, Mid Cap etc |
| plan | Text | Direct/Regular |

---

## 2. nav_history

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | Integer | Scheme Code |
| date | Date | NAV Date |
| nav | Decimal | Net Asset Value |

---

## 3. investor_transactions

| Column | Type | Description |
|---------|------|-------------|
| investor_id | Text | Investor ID |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Decimal | Transaction Amount |
| state | Text | Investor State |

---

## 4. scheme_performance

| Column | Type | Description |
|---------|------|-------------|
| return_1yr_pct | Decimal | 1 Year Return |
| return_3yr_pct | Decimal | 3 Year Return |
| return_5yr_pct | Decimal | 5 Year Return |
| expense_ratio_pct | Decimal | Expense Ratio |
| aum_crore | Integer | Assets Under Management |