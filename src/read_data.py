
from pathlib import Path
import pandas as pd

# Trouver automatiquement le dossier du projet
project_dir = Path(__file__).resolve().parent.parent

# Lire le fichier CSV
csv_path = project_dir / "data" / "orders.csv"
df = pd.read_csv(csv_path)

# Afficher les premières commandes
print("PREMIERES COMMANDES")
print(df.head())

# Afficher les dimensions du fichier
print("\nDIMENSIONS")
print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

# Calculer le montant de chaque commande
df["gross_amount"] = df["quantity"] * df["unit_price"]

print("\nMONTANT PAR COMMANDE")
print(df[["order_id", "gross_amount"]])

print("\nMONTANT BRUT TOTAL")
print(round(df["gross_amount"].sum(), 2))
