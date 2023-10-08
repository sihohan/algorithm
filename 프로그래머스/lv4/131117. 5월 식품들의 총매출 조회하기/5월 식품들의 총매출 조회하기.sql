-- 코드를 입력하세요
SELECT T1.PRODUCT_ID
, T1.PRODUCT_NAME
, SUM(T1.PRICE * T2.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT AS T1 INNER JOIN FOOD_ORDER AS T2
ON T1.PRODUCT_ID = T2.PRODUCT_ID
WHERE DATE_FORMAT(T2.PRODUCE_DATE, '%Y-%m-%d') LIKE '2022-05%'
GROUP BY T1.PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, T1.PRODUCT_ID ASC;