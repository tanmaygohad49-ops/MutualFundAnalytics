-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT substr(date,1,7) AS Month,
AVG(nav) AS Avg_NAV
FROM nav_history
GROUP BY Month;

-- 3. Total SIP Amount
SELECT SUM(amount_inr) AS Total_SIP
FROM investor_transactions
WHERE transaction_type='SIP';

-- 4. Transactions by State
SELECT state,
COUNT(*) AS Transactions
FROM investor_transactions
GROUP BY state
ORDER BY Transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Return by Category
SELECT category,
AVG(return_3yr_pct)
FROM scheme_performance
GROUP BY category;

-- 7. Top Fund Houses by AUM
SELECT fund_house,
SUM(aum_crore)
FROM scheme_performance
GROUP BY fund_house
ORDER BY SUM(aum_crore) DESC;

-- 8. Average Transaction Amount
SELECT AVG(amount_inr)
FROM investor_transactions;

-- 9. Number of Investors by State
SELECT state,
COUNT(DISTINCT investor_id)
FROM investor_transactions
GROUP BY state;

-- 10. Highest NAV
SELECT amfi_code,
MAX(nav)
FROM nav_history
GROUP BY amfi_code;