from outils import convertir_note, moyenne, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes_valides = []
notes_ignorees = 0

for texte in notes_brutes:
    note = convertir_note(texte)
    if note is not None:
        notes_valides.append(note)
    else:
        notes_ignorees += 1

moy = moyenne(notes_valides)
ment = mention(moy)

print(f"Notes ignorées : {notes_ignorees}")
print(f"Moyenne : {moy:.2f}")
print(f"Mention : {ment}")
