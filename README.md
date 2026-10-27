# Python pour l'analyse de données

Ce dépôt regroupe l'ensemble des exercices pratiques du module **Python pour l'analyse de données** : des fondamentaux de la programmation en Python (types, conditions, listes, dictionnaires, modularité) jusqu'à l'exploration, le nettoyage, l'agrégation, la jointure temporelle et la visualisation de données réelles avec **pandas**, **Matplotlib** et **Seaborn**.

## 📁 Arborescence des 12 exercices

```text
python-exercices/
├── exercice-01/
│   └── exercice.py          # Exercice 01 : Variables et calculs
├── exercice-02/
│   └── exercice.py          # Exercice 02 : Classer avec des conditions
├── exercice-03/
│   └── exercice.py          # Exercice 03 : Une semaine de températures (listes et boucles)
├── exercice-04/
│   └── exercice.py          # Exercice 04 : Le chiffre d'affaires d'un café (dictionnaires)
├── exercice-05/
│   ├── outils.py            # Exercice 05 : Fonctions utilitaires
│   └── main.py              # Exercice 05 : Script principal (modules et exceptions)
├── exercice-06/
│   └── exercice.ipynb       # Exercice 06 : Premier contact avec le Titanic (inspection)
├── exercice-07/
│   └── exercice.ipynb       # Exercice 07 : Interroger les passagers (filtres et tris)
├── exercice-08/
│   └── exercice.ipynb       # Exercice 08 : Nettoyer et justifier (manquants et doublons)
├── exercice-09/
│   └── exercice.ipynb       # Exercice 09 : Répondre à des questions (groupby et tableaux croisés)
├── exercice-10/
│   └── exercice.ipynb       # Exercice 10 : Enrichir par une jointure (merge de tables)
├── exercice-11/
│   └── exercice.ipynb       # Exercice 11 : Un mois de taxis à New York (séries temporelles)
├── exercice-12/
│   └── exercice.ipynb       # Exercice 12 : Cinq graphiques, cinq réponses (visualisation)
├── data/                    # Données nettoyées (ex. titanic_propre.csv)
├── figures/                 # Graphiques générés (sauvegarde PNG)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Configuration de l'environnement

1. **Création de l'environnement virtuel :**
   ```bash
   python3 -m venv .venv
   ```

2. **Activation de l'environnement virtuel :**
   - Sur macOS/Linux :
     ```bash
     source .venv/bin/activate
     ```
   - Sur Windows :
     ```bash
     .venv\Scripts\activate
     ```

3. **Installation des dépendances :**
   ```bash
   pip install -r requirements.txt
   ```
