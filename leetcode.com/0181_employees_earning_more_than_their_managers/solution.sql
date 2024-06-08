SELECT m.name AS Employee
FROM Employee AS m
JOIN Employee AS e ON e.id = m.managerId
WHERE m.salary > e.salary
