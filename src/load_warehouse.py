
import psycopg

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "ecommerce_dw",
    "user": "ecommerce_user",
    "password": "ecommerce_dev_password",
}

with psycopg.connect(**DB_CONFIG) as conn:
    with conn.cursor() as cur:

        # 1. Charger les clients uniques
        cur.execute("""
            INSERT INTO dim_customers (customer_id)
            SELECT DISTINCT customer_id
            FROM orders
            ON CONFLICT (customer_id) DO NOTHING;
        """)

        # 2. Charger les produits uniques
        cur.execute("""
            INSERT INTO dim_products (product_id)
            SELECT DISTINCT product_id
            FROM orders
            ON CONFLICT (product_id) DO NOTHING;
        """)

        # 3. Charger les commandes dans la table de faits
        cur.execute("""
            INSERT INTO fact_orders (
                order_id, order_date, customer_key, product_key,
                quantity, unit_price, country, status, gross_amount
            )
            SELECT
                o.order_id,
                o.order_date,
                c.customer_key,
                p.product_key,
                o.quantity,
                o.unit_price,
                o.country,
                o.status,
                o.quantity * o.unit_price
            FROM orders o
            JOIN dim_customers c
                ON o.customer_id = c.customer_id
            JOIN dim_products p
                ON o.product_id = p.product_id
            ON CONFLICT (order_id) DO NOTHING;
        """)

        # 4. Afficher les nombres de lignes chargées
        for table in ("dim_customers", "dim_products", "fact_orders"):
            cur.execute(f"SELECT COUNT(*) FROM {table};")
            print(f"{table}: {cur.fetchone()[0]} lignes")

print("Chargement du Data Warehouse terminé.")
