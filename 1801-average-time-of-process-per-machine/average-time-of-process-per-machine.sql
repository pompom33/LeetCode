SELECT machine_id, 
        ROUND(
            AVG(
                CASE WHEN activity_type='start' THEN - timestamp ELSE timestamp end
                )*2,
                3) AS processing_time
FROM activity
GROUP BY machine_id;