
# Exception parent pour toutes les erreurs de réservation
class ReservationException(Exception):

    def __init__(self, message):
        super().__init__(message)


# Exception si la capacité maximale est dépassée
class CapaciteDepasseeException(ReservationException):
    pass


# Exception si le nombre de places est incorrect
class NombreInvalideException(ReservationException):
    pass


# Exception si le nom du client est vide
class NomClientInvalideException(ReservationException):
    pass


# Classe qui représente un événement
class Evenement:

    def __init__(self, nom, capacite):

        if capacite <= 0:
            raise NombreInvalideException(
                "La capacité doit être positive."
            )

        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0

    # Méthode pour effectuer une réservation
    def reserver(self, nom_client, nb_places):

        # Vérifier le nom du client
        if not nom_client.strip():
            raise NomClientInvalideException(
                "Le nom du client est obligatoire."
            )

        # Vérifier le nombre de places demandé
        if nb_places <= 0:
            raise NombreInvalideException(
                "Le nombre de places doit être positif."
            )

        # Vérifier la capacité restante
        if self.places_reservees + nb_places > self.capacite:
            raise CapaciteDepasseeException(
                "La capacité maximale de l'événement est dépassée."
            )

        # La réservation est valide : on met à jour le compteur
        self.places_reservees += nb_places

        print(
            f"Réservation confirmée pour {nom_client} "
            f"({nb_places} places)."
        )

    # Afficher les informations de l'événement
    def afficher(self):

        print(
            f"Événement : {self.nom} | "
            f"{self.places_reservees}/{self.capacite} "
            f"places réservées"
        )
