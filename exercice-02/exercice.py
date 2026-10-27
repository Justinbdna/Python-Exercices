# --- Classification des températures ---
temperatures = [-3, 0, 15, 31]
for temperature in temperatures:
    if temperature < 0:
        statut = "gel"
    elif temperature < 15:
        statut = "froid"
    elif temperature < 25:
        statut = "doux"
    else:
        statut = "chaud"
    print(f"{temperature} °C : {statut}")
print()

# --- Années bissextiles ---
annees = [2024, 1900, 2000]
for annee in annees:
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        resultat = "bissextile"
    else:
        resultat = "non bissextile"
    print(f"{annee} : {resultat}")