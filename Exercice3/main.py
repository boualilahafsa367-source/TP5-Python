
# Importation de la fonction et des exceptions
from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


# Programme principal
if __name__ == "__main__":

    print("=== Importation des articles CSV ===")

    try:
        # Charger les articles depuis le fichier
        articles = charger_csv("articles.csv")

        print("Importation réussie !")

        # Afficher les articles importés
        for article in articles:
            print(
                f"ID : {article['id']} | "
                f"Nom : {article['nom']} | "
                f"Prix : {article['prix']:.2f} DH"
            )

        print(f"Nombre total d'articles : {len(articles)}")

    except FichierIntrouvableException as erreur:
        print("Erreur de fichier :", erreur)

    except LigneInvalideException as erreur:
        print("Erreur de format :", erreur)

    except PrixNegatifException as erreur:
        print("Erreur de prix :", erreur)
