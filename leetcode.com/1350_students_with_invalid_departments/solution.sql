SELECT id, name
FROM students
WHERE department_id NOT IN (SELECT id FROM Departments)
