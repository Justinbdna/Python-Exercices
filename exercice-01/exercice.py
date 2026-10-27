# Données initial
produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2

# Calcul initial
total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

# Donnée sous forme de texte et conversion explicite
prix_texte = "19.90"
prix_ht = float(prix_texte)

# Recalcul avec le prix converti
total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

# Affichage du résultat formaté
print(f"{quantite} x {produit} : {total_ttc:.2f} euros TTC")
