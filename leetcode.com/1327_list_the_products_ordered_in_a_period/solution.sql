SELECT product_name, SUM(unit) as unit
FROM Products AS p
JOIN Orders AS o ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY product_name
HAVING SUM(unit) >= 100
