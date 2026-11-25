# Exercice 1 : Exceptions personnalisées avec un compte bancaire

**Figure 1 : Exécution du programme – Gestion des erreurs d'un compte bancaire**

<img width="1920" height="561" alt="image" src="https://github.com/user-attachments/assets/4ef5e33f-9f58-442e-9de2-29fe9e265f7a" />


Dans cet exercice, nous avons créé une classe `CompteBancaire` permettant de gérer les opérations d'un compte bancaire, notamment les dépôts et les retraits.

Nous avons également défini deux exceptions personnalisées :

- `SoldeInsuffisantException` : déclenchée lorsqu'un retrait dépasse le solde disponible.
- `MontantNegatifException` : déclenchée lorsqu'un montant de dépôt ou de retrait est nul ou négatif.

La méthode `deposer()` vérifie que le montant est positif avant de modifier le solde. La méthode `retirer()` vérifie également la validité du montant et la disponibilité de l'argent avant d'effectuer le retrait.

Dans le programme de test, nous avons créé un compte avec un solde initial de 1250 DH, effectué un dépôt de 350 DH et un retrait de 200 DH, puis essayé de retirer un montant supérieur au solde disponible.

Le résultat obtenu montre que les opérations valides sont exécutées normalement, tandis que le retrait impossible déclenche une exception personnalisée qui est récupérée avec `try` et `except`.

Cet exercice permet de comprendre comment créer ses propres exceptions pour gérer des erreurs spécifiques à une application.

# Exercice 2 : Exceptions personnalisées avec un système de réservation

**Figure 2 : Exécution du programme – Gestion des réservations et de la capacité**

<img width="1920" height="611" alt="image" src="https://github.com/user-attachments/assets/4e9a9f93-ce17-42d5-ba3b-54c9f26f3860" />


Dans cet exercice, nous avons développé un système de réservation de places pour un événement à l'aide de la classe `Evenement`.

Cette classe contient le nom de l'événement, sa capacité maximale et le nombre de places déjà réservées.

Nous avons créé une hiérarchie d'exceptions composée d'une exception parent `ReservationException` et de trois exceptions spécialisées :

- `CapaciteDepasseeException` : lorsque le nombre total de places demandées dépasse la capacité maximale.
- `NombreInvalideException` : lorsque le nombre de places est nul ou négatif.
- `NomClientInvalideException` : lorsque le nom du client est vide ou contient uniquement des espaces.

La méthode `reserver()` effectue ces différentes vérifications avant de confirmer une réservation et de mettre à jour le nombre de places réservées.

Pour les tests, nous avons créé un événement nommé « Atelier Python » avec une capacité de 12 places. Deux réservations ont été effectuées avec succès, puis une troisième réservation a été refusée car elle dépassait la capacité restante.

Le programme utilise plusieurs blocs `except` pour récupérer les erreurs spécifiques, ainsi qu'un bloc permettant de récupérer plus généralement les exceptions de type `ReservationException`.

Cet exercice montre l'intérêt de l'héritage pour organiser les exceptions en plusieurs catégories et faciliter leur gestion.


# Exercice 3 : Import CSV sécurisé avec des exceptions personnalisées

**Figure 3 : Exécution du programme – Importation et validation des articles CSV**

<img width="1920" height="659" alt="image" src="https://github.com/user-attachments/assets/5632d5c2-16e7-489c-ab1f-cbfe3296f5fc" />

<img width="1920" height="657" alt="image" src="https://github.com/user-attachments/assets/026429c4-3db2-48b2-9523-b278b47c580c" />


Dans cet exercice, nous avons conçu un système d'importation sécurisé de fichiers CSV contenant des informations sur des articles, notamment leur identifiant, leur nom et leur prix.

L'architecture du programme est organisée en trois fichiers Python :

- `csv_reader.py` : contient les exceptions personnalisées et la fonction `charger_csv()`, responsable de la lecture et de la validation des données.
- `main.py` : représente le point d'entrée du programme et gère les différentes erreurs.
- `tests_csv.py` : contient les tests unitaires permettant de vérifier le comportement du système.

Nous avons défini une exception parent `CsvException` et trois exceptions spécialisées :

- `FichierIntrouvableException` : lorsque le fichier demandé n'existe pas.
- `LigneInvalideException` : lorsqu'une ligne ne respecte pas le format attendu ou contient un prix non numérique.
- `PrixNegatifException` : lorsque le prix est nul ou négatif.

La fonction `charger_csv()` vérifie l'existence du fichier, lit son contenu à l'aide du module `csv`, contrôle le nombre de colonnes et convertit les prix en nombres décimaux. Les lignes vides sont ignorées et les articles valides sont stockés dans une liste de dictionnaires.

Nous avons utilisé un fichier `articles.csv` contenant trois articles de démonstration : Clavier, Souris et Ecran. L'exécution du programme affiche les informations importées ainsi que le nombre total d'articles.

Enfin, nous avons créé plusieurs tests unitaires avec le module `unittest` pour vérifier les différents scénarios : fichier valide, fichier absent, prix non numérique, prix négatif, colonne manquante et ligne vide. Des fichiers temporaires sont utilisés afin de réaliser les tests sans modifier le fichier CSV principal.

Cet exercice permet de mettre en pratique la gestion avancée des exceptions, la validation des données, la manipulation des fichiers et les tests automatisés.

