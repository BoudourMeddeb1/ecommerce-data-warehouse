
from pathlib import Path
import pandas as pd
import psycopg

# Chemin du projet et du fichier CSV
project_dir = Path(__file__).resolve().parent.parent
csv_path = project_dir / "data" / "orders.csv"

# Lire le CSV
df = pd.read_csv(csv_path)

# Connexion à PostgreSQL
with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="ecommerce_dw",
    user="ecommerce_user",
    password="ecommerce_dev_password",
) as conn:

    with conn.cursor() as cur:
        # Charger chaque commande dans la table orders
        for _, row in df.iterrows():
            cur.execute(
                """
                INSERT INTO orders (
                    order_id, order_date, customer_id, product_id,
                    quantity, unit_price, country, status
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (order_id) DO NOTHING;
                """,
                (
                    int(row["order_id"]),
                    row["order_date"],
                    row["customer_id"],
                    row["product_id"],
                    int(row["quantity"]),
                    float(row["unit_price"]),
                    row["country"],
                    row["status"],
                ),
            )

print(f"{len(df)} commandes lues depuis le CSV.")
print("Chargement terminé.")
