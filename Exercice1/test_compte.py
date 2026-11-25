
# Importation de la classe et des exceptions
from compte_bancaire import (
    CompteBancaire,
    SoldeInsuffisantException,
    MontantNegatifException
)


# Création d'un compte avec un solde initial personnalisé
compte = CompteBancaire("Salma", 1250)

try:
    print("=== Gestion du compte bancaire ===")

    compte.afficher()

    # Effectuer un dépôt
    compte.deposer(350)

    # Effectuer un retrait valide
    compte.retirer(200)

    compte.afficher()

    # Essayer un retrait supérieur au solde disponible
    compte.retirer(2000)

except SoldeInsuffisantException as erreur:
    print("Erreur de solde :", erreur)

except MontantNegatifException as erreur:
    print("Erreur de montant :", erreur)
