SELECT order_id, COUNT(*) AS occurrences
FROM fact_orders
GROUP BY order_id
HAVING COUNT(*) > 1;
SELECT order_id, quantity, unit_price, gross_amount
FROM fact_orders
WHERE gross_amount <> quantity * unit_price;
SELECT *
FROM fact_orders
WHERE order_date IS NULL
   OR customer_key IS NULL
   OR product_key IS NULL
   OR quantity IS NULL
   OR unit_price IS NULL
   OR gross_amount IS NULL;
SELECT *
FROM fact_orders
WHERE quantity <= 0
   OR unit_price < 0;   