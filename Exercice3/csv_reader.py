
# Module pour lire les fichiers CSV
import csv

# Permet de vérifier si un fichier existe
import os


# Exception parent pour toutes les erreurs CSV
class CsvException(Exception):

    def __init__(self, message):
        super().__init__(message)


# Exception si le fichier est introuvable
class FichierIntrouvableException(CsvException):
    pass


# Exception si une ligne ne respecte pas le format
class LigneInvalideException(CsvException):
    pass


# Exception si le prix est négatif ou nul
class PrixNegatifException(CsvException):
    pass


# Fonction qui charge et valide les articles du fichier CSV
def charger_csv(chemin):

    # Vérifier si le fichier existe
    if not os.path.isfile(chemin):
        raise FichierIntrouvableException(
            f"Le fichier '{chemin}' est introuvable."
        )

    articles = []

    # Ouvrir le fichier avec le séparateur point-virgule
    with open(chemin, "r", encoding="utf-8", newline="") as fichier:

        lecteur = csv.reader(fichier, delimiter=";")

        # Lire et vérifier l'en-tête
        try:
            entete = next(lecteur)
        except StopIteration:
            raise LigneInvalideException("Le fichier CSV est vide.")

        if entete != ["id", "nom", "prix"]:
            raise LigneInvalideException(
                "L'en-tête doit être : id;nom;prix."
            )

        # Lire chaque ligne du fichier
        for numero, ligne in enumerate(lecteur, start=2):

            # Ignorer les lignes vides
            if not ligne or all(not valeur.strip() for valeur in ligne):
                continue

            # Vérifier le nombre de colonnes
            if len(ligne) != 3:
                raise LigneInvalideException(
                    f"Ligne {numero} : trois colonnes sont nécessaires."
                )

            identifiant, nom, prix_texte = [
                valeur.strip() for valeur in ligne
            ]

            # Vérifier que l'identifiant et le nom existent
            if not identifiant or not nom:
                raise LigneInvalideException(
                    f"Ligne {numero} : identifiant ou nom manquant."
                )

            # Convertir le prix en nombre décimal
            try:
                prix = float(prix_texte)
            except ValueError:
                raise LigneInvalideException(
                    f"Ligne {numero} : le prix doit être numérique."
                )

            # Le prix doit être strictement positif
            if prix <= 0:
                raise PrixNegatifException(
                    f"Ligne {numero} : le prix doit être supérieur à zéro."
                )

            # Ajouter l'article sous forme de dictionnaire
            article = {
                "id": identifiant,
                "nom": nom,
                "prix": prix
            }

            articles.append(article)

    return articles
