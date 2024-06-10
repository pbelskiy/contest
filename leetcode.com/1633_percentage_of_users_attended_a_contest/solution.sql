SELECT
    r.contest_id,
    ROUND((
        CAST(COUNT(r.user_id) AS float) /
        CAST((SELECT COUNT(DISTINCT user_id) FROM Users) AS float) * 100)::numeric, 2
    ) AS percentage
FROM Users AS u
JOIN Register AS r ON r.user_id = u.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC
