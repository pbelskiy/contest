SELECT p.product_name, s.year, s.price
FROM Sales AS s
JOIN Product AS p on p.product_id = s.product_id
