SELECT P.project_id, ROUND(AVG(E.experience_years), 2) AS average_years
FROM Employee AS E
JOIN Project AS P ON E.employee_id = P.employee_id
GROUP BY P.project_id
