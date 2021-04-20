SELECT p.FirstName, p.LastName, a.City, a.State
FROM Address AS a
RIGHT JOIN Person AS p ON p.PersonId = a.PersonId
