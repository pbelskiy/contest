SELECT u.name, SUM(t.amount) AS balance FROM Users AS u
JOIN Transactions AS t ON t.account = u.account
GROUP BY u.name
HAVING balance > 10000
