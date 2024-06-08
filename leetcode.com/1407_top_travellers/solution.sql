SELECT u.name, travelled_distance
FROM (
    SELECT u.id, SUM(coalesce(r.distance, 0)) travelled_distance
    FROM Users AS u
    LEFT JOIN Rides AS r ON u.id = r.user_id
    GROUP BY u.id
) AS s
JOIN Users AS u ON u.id = s.id
ORDER BY travelled_distance DESC, u.name
