def convertir_note(texte):
    """Convertit une note au format texte (avec virgule ou point) en float, ou renvoie None si invalide."""
    try:
        return float(texte.replace(",", "."))
    except (ValueError, AttributeError):
        return None


def moyenne(valeurs):
    """Calcule la moyenne d'une liste de nombres."""
    if not valeurs:
        return 0.0
    return sum(valeurs) / len(valeurs)


def mention(note):
    """Renvoie la mention associée à une note."""
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    else:
        return "Aucune"
