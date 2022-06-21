# Write your MySQL query statement below
SELECT name, IF(distance IS NULL, 0, SUM(distance)) AS travelled_distance
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY user_id
ORDER BY travelled_distance DESC, name ASC
