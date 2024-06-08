SELECT
    user_id,
    upper(substring(name from 1 for 1)) ||
    lower(substring(name from 2 for length(name))) name
FROM Users
ORDER BY user_id
