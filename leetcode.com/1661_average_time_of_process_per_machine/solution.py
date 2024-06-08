SELECT
    machine_id,
    ROUND(AVG(d)::numeric, 3) AS processing_time
FROM (
    SELECT
        a.machine_id,
        a.process_id,
        (b.timestamp - a.timestamp) AS d
    FROM Activity AS a
    JOIN Activity AS b
        ON a.machine_id = b.machine_id AND a.process_id = b.process_id
    WHERE
        a.activity_type = 'start' AND
        b.activity_type = 'end'
)
GROUP BY machine_id
ORDER BY machine_id
