# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit
FROM Orders o JOIN Products p ON o.product_id = p.product_id
WHERE MONTH(order_date) = MONTH("2020-02-01") AND YEAR(order_date) = YEAR("2020-02-01")
GROUP BY o.product_id
HAVING unit >= 100
