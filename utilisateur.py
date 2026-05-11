# =============================================================
# utilisateur.py
# Fichier contenant la classe Utilisateur
# =============================================================
# Une classe est un "moule" pour créer des objets.
# Ici, le moule "Utilisateur" permettra de créer autant
# d'utilisateurs qu'on veut, chacun avec ses propres données.
# =============================================================


# Liste des rôles autorisés (constante définie en dehors de la classe
# pour pouvoir être réutilisée ailleurs si besoin)
ROLES_AUTORISES = ["Data Analyst", "Data Engineer", "DBA", "Administrateur"]


class Utilisateur:
    """
    Représente un utilisateur de l'application de gestion des datasets.

    Attributs :
    -----------
    id_user  : str  → identifiant unique de l'utilisateur (ex: "U001")
    nom      : str  → nom complet (ex: "Alice Dupont")
    email    : str  → adresse email (ex: "alice@data.com")
    role     : str  → rôle dans l'équipe (parmi ROLES_AUTORISES)
    """

    def __init__(self, id_user, nom, email, role):
        """
        Constructeur : appelé automatiquement à la création d'un objet.

        'self' représente l'objet en cours de création.
        Chaque attribut (self.xxx) est propre à cet objet.

        Exemple d'appel :
            u1 = Utilisateur("U001", "Alice", "alice@data.com", "DBA")
        """
        # Vérification du rôle avant de l'assigner
        if role not in ROLES_AUTORISES:
            raise ValueError(
                f"Rôle invalide : '{role}'. "
                f"Rôles autorisés : {ROLES_AUTORISES}"
            )

        self.id_user = id_user   # Identifiant unique de l'utilisateur
        self.nom = nom           # Nom de l'utilisateur
        self.email = email       # Email de l'utilisateur
        self.role = role         # Rôle (Data Analyst, DBA, etc.)

    def afficher_infos(self):
        """
        Affiche les informations de l'utilisateur dans la console
        de manière lisible et formatée.

        Cette méthode ne retourne rien (None), elle affiche directement.
        """
        print("=" * 40)
        print("       INFORMATIONS UTILISATEUR")
        print("=" * 40)
        print(f"  ID      : {self.id_user}")
        print(f"  Nom     : {self.nom}")
        print(f"  Email   : {self.email}")
        print(f"  Rôle    : {self.role}")
        print("=" * 40)

    def __str__(self):
        """
        Méthode spéciale appelée automatiquement quand on fait :
            print(utilisateur)  ou  str(utilisateur)

        Elle retourne une représentation textuelle de l'objet.
        """
        return f"Utilisateur[{self.id_user}] {self.nom} ({self.role})"