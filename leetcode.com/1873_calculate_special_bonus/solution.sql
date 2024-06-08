    SELECT
        employee_id,
        salary AS bonus
    FROM
        Employees
    WHERE
        MOD(employee_id, 2) = 1 AND
        SUBSTRING(name, 1, 1) != 'M'
UNION
    SELECT
        employee_id,
        0 AS bonus
    FROM
        Employees
    WHERE
        NOT(
            MOD(employee_id, 2) = 1 AND
            SUBSTRING(name, 1, 1) != 'M'
        )
ORDER BY employee_id
