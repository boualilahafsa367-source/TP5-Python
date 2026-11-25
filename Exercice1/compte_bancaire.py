
# Exception personnalisée pour un solde insuffisant
class SoldeInsuffisantException(Exception):

    def __init__(self, message):
        # Transmet le message à la classe Exception
        super().__init__(message)


# Exception personnalisée pour un montant de dépôt invalide
class MontantNegatifException(Exception):

    def __init__(self, message):
        super().__init__(message)


# Classe qui représente un compte bancaire
class CompteBancaire:

    def __init__(self, nom, solde=0):
        if solde < 0:
            raise MontantNegatifException(
                "Le solde initial ne peut pas être négatif."
            )

        self.nom = nom
        self.solde = solde

    # Méthode pour déposer de l'argent
    def deposer(self, montant):

        if montant <= 0:
            raise MontantNegatifException(
                "Le montant du dépôt doit être positif."
            )

        self.solde += montant
        print(f"Dépôt de {montant:.2f} DH effectué.")

    # Méthode pour retirer de l'argent
    def retirer(self, montant):

        if montant <= 0:
            raise MontantNegatifException(
                "Le montant du retrait doit être positif."
            )

        if montant > self.solde:
            raise SoldeInsuffisantException(
                "Solde insuffisant pour effectuer ce retrait."
            )

        self.solde -= montant
        print(f"Retrait de {montant:.2f} DH effectué.")

    # Méthode pour afficher le compte
    def afficher(self):
        print(f"Compte : {self.nom}, Solde : {self.solde:.2f} DH")
