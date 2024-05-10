SELECT NULLIF((
    SELECT num FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
    ORDER BY -num
    LIMIT 1
), NULL) AS num
