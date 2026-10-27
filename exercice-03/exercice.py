# Données Températures
temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

# Moyenne, minimum et maximum
moyenne = sum(temperatures) / len(temperatures)
min_temp = min(temperatures)
max_temp = max(temperatures)
print(f"Moyenne : {moyenne:.2f}")
print(f"Min : {min_temp} / Max : {max_temp}")

# Compter les jours > 15 °C avec une boucle
jours_chauds = 0
for t in temperatures:
    if t > 15:
        jours_chauds += 1
print(f"Jours > 15 °C : {jours_chauds}")

# Construire la liste en Fahrenheit
fahrenheit = [round(c * 9 / 5 + 32, 1) for c in temperatures]
print(f"Fahrenheit : {fahrenheit}")

# Afficher chaque jour avec enumerate
for i, t in enumerate(temperatures, start=1):
    print(f"Jour {i} : {t} °C")