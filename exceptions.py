# =============================================================
# exceptions.py
# Fichier contenant toutes les exceptions personnalisées du projet
# =============================================================
# En Python, on peut créer ses propres exceptions en héritant
# de la classe de base "Exception". Cela permet de signaler des
# erreurs précises et compréhensibles dans notre application.
# =============================================================


class DatasetIntrouvableException(Exception):
    """
    Levée quand on cherche un dataset qui n'existe pas dans le gestionnaire.
    Exemple : rechercher l'id "DS99" alors qu'il n'est pas enregistré.
    """
    pass  # 'pass' signifie qu'on n'ajoute rien : le message sera fourni
          # lors du raise, ex: raise DatasetIntrouvableException("DS99 introuvable")


class TailleDatasetInvalideException(Exception):
    """
    Levée quand la taille fournie pour un dataset est invalide.
    Règle métier : la taille doit être STRICTEMENT supérieure à 0.
    Exemple : taille = -5 ou taille = 0 → exception levée.
    """
    pass


class TypeDatasetInvalideException(Exception):
    """
    Levée quand le type de données fourni n'est pas dans la liste autorisée.
    Liste autorisée : ["CSV", "JSON", "SQL", "IMAGE", "LOG"]
    Exemple : type = "EXCEL" → exception levée.
    """
    pass
