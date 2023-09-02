(
  SELECT MAX(salary) AS SecondHighestSalary FROM Employee
  WHERE salary != (SELECT salary FROM Employee ORDER BY salary DESC LIMIT 1)
  ORDER BY salary LIMIT 1
) UNION SELECT NULL LIMIT 1;
