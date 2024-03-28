import csv
from collections import defaultdict

def lire_lignes_en_double(nom_fichier):
    lignes_compteur = defaultdict(int)  # Utilisation d'un dictionnaire pour compter le nombre d'occurrences de chaque ligne
    with open(nom_fichier, newline='') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        for ligne in lecteur_csv:
            lignes_compteur[tuple(ligne)] += 1  # Convertir la liste de ligne en tuple pour être hashable, puis compter les occurrences

    for ligne, compteur in lignes_compteur.items():
        if compteur > 1:  # Afficher uniquement les lignes qui apparaissent plus d'une fois
            print(','.join(ligne))  # Imprimer la ligne

# Remplacez 'votre_fichier.csv' par le chemin de votre fichier CSV
nom_fichier_csv = 'dns.csv'
lire_lignes_en_double(nom_fichier_csv)
