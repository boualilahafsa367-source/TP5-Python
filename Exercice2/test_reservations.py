
# Importation de la classe et des exceptions
from reservations import (
    Evenement,
    ReservationException,
    CapaciteDepasseeException,
    NombreInvalideException,
    NomClientInvalideException
)


# Création d'un événement avec une capacité personnalisée
evenement = Evenement("Atelier Python", 12)

print("=== Gestion des réservations ===")

try:
    # Première réservation : 4 places
    evenement.reserver("Imane", 4)

    # Deuxième réservation : 5 places
    evenement.reserver("Yassine", 5)

    evenement.afficher()

    # Cette réservation dépasse la capacité restante
    evenement.reserver("Meriem", 5)

except CapaciteDepasseeException as erreur:
    print("Erreur de capacité :", erreur)

except NombreInvalideException as erreur:
    print("Erreur de nombre :", erreur)

except NomClientInvalideException as erreur:
    print("Erreur de nom :", erreur)

except ReservationException as erreur:
    # Récupère toute autre erreur appartenant à cette famille
    print("Erreur de réservation :", erreur)
