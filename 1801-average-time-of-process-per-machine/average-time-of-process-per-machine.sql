/* Write your PL/SQL query statement below */
SELECT E.machine_id, 
        ROUND(AVG(E.timestamp - S.timestamp), 3) AS processing_time
FROM Activity E
JOIN Activity S
    ON E.machine_id = S.machine_id 
WHERE S.activity_type = 'start' AND E.activity_type = 'end'
GROUP BY E.machine_id;
