#Données ventes
ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]
# Dictionnaire ca_par_produit (produit: prix * quantité)
ca_par_produit = {item["produit"]: item["prix"] * item["quantite"] for item in ventes}
print(ca_par_produit)

#Chiffre d'affaires total
total_ca = sum(ca_par_produit.values())
print(f"Total : {total_ca:.2f} euros")

# Produit qui rapporte le plus
meilleur_produit = max(ca_par_produit, key=ca_par_produit.get)
print(f"Meilleur produit : {meilleur_produit}")
