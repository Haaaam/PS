SELECT PRODUCT_ID,PRODUCT_TIME,PRODUCT_CD,CATEGORY,PRICE
FROM FOOD_PRODUCT
WHERE PRICE=(
    SELECT MAX(PRICE)
    FROM FOOD_PRODUCT
);