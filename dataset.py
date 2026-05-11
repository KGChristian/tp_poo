# =============================================================
# dataset.py
# Fichier contenant la classe Dataset
# =============================================================
# On importe les exceptions qu'on a créées dans exceptions.py
# Le mot-clé 'from ... import ...' permet de récupérer uniquement
# ce dont on a besoin depuis un autre fichier.
# =============================================================

from exceptions import TailleDatasetInvalideException, TypeDatasetInvalideException


# Liste des types de données autorisés pour un dataset
TYPES_AUTORISES = ["CSV", "JSON", "SQL", "IMAGE", "LOG"]

# Seuil (en Mo) au-delà duquel un dataset est considéré comme volumineux
SEUIL_VOLUMINEUX = 1000  # Mo


class Dataset:
    """
    Représente un jeu de données (dataset) géré par l'application.

    Attributs :
    -----------
    id_dataset   : str         → identifiant unique du dataset (ex: "DS001")
    nom          : str         → nom descriptif (ex: "Ventes 2024")
    source       : str         → origine des données (ex: "PostgreSQL", "API REST")
    taille_mo    : float       → taille en mégaoctets (doit être > 0)
    type_donnees : str         → format des données (parmi TYPES_AUTORISES)
    proprietaire : Utilisateur → objet Utilisateur qui possède ce dataset
    """

    def __init__(self, id_dataset, nom, source, taille_mo, type_donnees, proprietaire):
        """
        Constructeur du Dataset.

        Avant d'assigner les valeurs, on valide :
        - que la taille est > 0 (sinon TailleDatasetInvalideException)
        - que le type est dans la liste autorisée (sinon TypeDatasetInvalideException)

        Exemple d'appel :
            ds = Dataset("DS001", "Logs serveur", "Syslog", 250.5, "LOG", user1)
        """

        # ----- VALIDATION DE LA TAILLE -----
        # On vérifie que la taille est un nombre positif strictement supérieur à 0
        if taille_mo <= 0:
            raise TailleDatasetInvalideException(
                f"La taille doit être supérieure à 0 Mo. Valeur reçue : {taille_mo} Mo"
            )

        # ----- VALIDATION DU TYPE -----
        # On convertit en majuscules pour éviter les erreurs de casse ("csv" → "CSV")
        type_donnees = type_donnees.upper()
        if type_donnees not in TYPES_AUTORISES:
            raise TypeDatasetInvalideException(
                f"Type '{type_donnees}' non reconnu. "
                f"Types autorisés : {TYPES_AUTORISES}"
            )

        # ----- ASSIGNATION DES ATTRIBUTS -----
        self.id_dataset = id_dataset         # Identifiant unique
        self.nom = nom                       # Nom du dataset
        self.source = source                 # Source des données
        self.taille_mo = taille_mo           # Taille en Mo (float)
        self.type_donnees = type_donnees     # Type validé et mis en majuscules
        self.proprietaire = proprietaire     # Objet Utilisateur (pas juste un nom !)

    def afficher_infos(self):
        """
        Affiche toutes les informations du dataset de manière lisible.
        
        On accède au propriétaire via self.proprietaire.nom
        car proprietaire est un objet Utilisateur (pas un simple texte).
        """
        print("-" * 45)
        print(f"  ID Dataset   : {self.id_dataset}")
        print(f"  Nom          : {self.nom}")
        print(f"  Source       : {self.source}")
        print(f"  Taille       : {self.taille_mo} Mo")
        print(f"  Type         : {self.type_donnees}")
        # On accède à l'attribut 'nom' de l'objet Utilisateur propriétaire
        print(f"  Propriétaire : {self.proprietaire.nom} ({self.proprietaire.role})")
        # Affichage conditionnel : volumineux ou non
        statut = "⚠ VOLUMINEUX" if self.est_volumineux() else "✓ Normal"
        print(f"  Statut taille: {statut}")
        print("-" * 45)

    def est_volumineux(self):
        """
        Retourne True si la taille du dataset dépasse 1000 Mo, False sinon.

        C'est une méthode "booléenne" : elle répond par Oui (True) ou Non (False).

        Exemple :
            ds.taille_mo = 1500 → est_volumineux() retourne True
            ds.taille_mo = 300  → est_volumineux() retourne False
        """
        return self.taille_mo > SEUIL_VOLUMINEUX

    def __str__(self):
        """
        Représentation textuelle courte du dataset.
        Appelée automatiquement par print(dataset) ou str(dataset).
        """
        volumineux_tag = " [VOLUMINEUX]" if self.est_volumineux() else ""
        return (
            f"Dataset[{self.id_dataset}] '{self.nom}' "
            f"| {self.type_donnees} | {self.taille_mo} Mo{volumineux_tag} "
            f"| Propriétaire: {self.proprietaire.nom}"
        )
