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
