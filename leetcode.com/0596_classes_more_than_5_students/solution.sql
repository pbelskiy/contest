# Write your MySQL query statement below

SELECT class
FROM (SELECT DISTINCT student, class FROM courses) AS _courses
GROUP BY class
HAVING COUNT(student) >= 5

