SELECT teacher_id, COUNT(subject_id) AS cnt
FROM (
    SELECT DISTINCT subject_id, teacher_id FROM Teacher
)
GROUP BY teacher_id
