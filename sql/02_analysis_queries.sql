SELECT
    SUM(gross_amount) AS total_revenue
FROM fact_orders;
SELECT
    SUM(gross_amount) AS completed_revenue
FROM fact_orders
WHERE status = 'completed';
SELECT
    country,
    SUM(gross_amount) AS revenue,
    COUNT(*) AS number_of_orders
FROM fact_orders
WHERE status = 'completed'
GROUP BY country
ORDER BY revenue DESC;
SELECT
    status,
    COUNT(*) AS number_of_orders
FROM fact_orders
GROUP BY status
ORDER BY number_of_orders DESC;
SELECT
    p.product_id,
    SUM(f.quantity) AS units_sold,
    SUM(f.gross_amount) AS total_revenue
FROM fact_orders f
JOIN dim_products p
    ON f.product_key = p.product_key
WHERE f.status = 'completed'
GROUP BY p.product_id
ORDER BY total_revenue DESC;
