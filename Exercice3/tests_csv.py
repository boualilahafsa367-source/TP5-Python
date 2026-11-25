
import unittest
import tempfile
import os

from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


class TestImportCSV(unittest.TestCase):

    # Créer un fichier temporaire contenant le texte fourni
    def creer_fichier(self, contenu):

        fichier = tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            suffix=".csv",
            delete=False
        )

        fichier.write(contenu)
        fichier.close()

        return fichier.name

    # Supprimer le fichier temporaire après chaque test
    def supprimer_fichier(self, chemin):

        if os.path.exists(chemin):
            os.remove(chemin)

    # Test 1 : fichier valide contenant trois articles
    def test_csv_valide(self):

        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "201;Casque;320.50\n"
            "202;Webcam;480.00\n"
            "203;Micro;275.90\n"
        )

        try:
            articles = charger_csv(chemin)

            self.assertEqual(len(articles), 3)
            self.assertEqual(articles[0]["nom"], "Casque")
            self.assertEqual(articles[0]["prix"], 320.50)

        finally:
            self.supprimer_fichier(chemin)

    # Test 2 : fichier inexistant
    def test_fichier_absent(self):

        with self.assertRaises(FichierIntrouvableException):
            charger_csv("fichier_inexistant.csv")

    # Test 3 : ligne avec un prix non numérique
    def test_prix_non_numerique(self):

        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "204;Clavier;abc\n"
        )

        try:
            with self.assertRaises(LigneInvalideException):
                charger_csv(chemin)

        finally:
            self.supprimer_fichier(chemin)

    # Test 4 : ligne avec un prix négatif
    def test_prix_negatif(self):

        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "205;Souris;-50\n"
        )

        try:
            with self.assertRaises(PrixNegatifException):
                charger_csv(chemin)

        finally:
            self.supprimer_fichier(chemin)

    # Test 5 : ligne avec une colonne manquante
    def test_colonne_manquante(self):

        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "206;Ecran\n"
        )

        try:
            with self.assertRaises(LigneInvalideException):
                charger_csv(chemin)

        finally:
            self.supprimer_fichier(chemin)

    # Test 6 : ligne vide ignorée
    def test_ligne_vide(self):

        chemin = self.creer_fichier(
            "id;nom;prix\n"
            "207;Clavier;250\n"
            "\n"
            "208;Souris;130\n"
        )

        try:
            articles = charger_csv(chemin)

            self.assertEqual(len(articles), 2)

        finally:
            self.supprimer_fichier(chemin)


# Exécution des tests
if __name__ == "__main__":
    unittest.main()
