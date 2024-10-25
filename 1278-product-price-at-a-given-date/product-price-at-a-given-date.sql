/* Write your PL/SQL query statement below */
WITH 
TEM1 AS (
    select product_id, new_price PRICE 
    from products 
    where (PRODUCT_ID, change_date)
    in (SELECT 
            PRODUCT_ID, 
            max(change_date) 
        FROM PRODUCTS 
        WHERE change_date<='2019-08-16' 
        GROUP BY PRODUCT_ID)),
TEM2 AS (
    SELECT PRODUCT_ID, 10 price 
    FROM PRODUCTS 
    WHERE PRODUCT_ID 
    NOT IN (SELECT PRODUCT_ID 
            FROM TEM1))
SELECT PRODUCT_ID, PRICE 
FROM TEM1 
UNION SELECT PRODUCT_ID, PRICE 
FROM TEM2;