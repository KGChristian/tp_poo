# =============================================================
# gestionnaire_dataset.py
# Fichier contenant la classe GestionnaireDataset
# =============================================================
# Cette classe joue le rôle de "registre central" de l'application.
# Elle stocke une liste de datasets et offre toutes les opérations
# courantes : ajout, affichage, recherche, suppression, filtrage...
#
# C'est le principe de "COMPOSITION" en POO :
# GestionnaireDataset contient (possède) une liste de Dataset.
# =============================================================

from exceptions import DatasetIntrouvableException


class GestionnaireDataset:
    """
    Gère une collection de datasets : stockage, recherche, filtrage, etc.

    Attribut :
    ----------
    datasets : list → liste d'objets Dataset gérés par cette instance
    """

    def __init__(self):
        """
        Constructeur : initialise la liste vide des datasets.
        
        On n'a pas besoin de paramètres : le gestionnaire démarre
        toujours avec une liste vide, qu'on remplira via ajouter_dataset().
        """
        self.datasets = []   # Liste vide au départ (type : list de Dataset)

    # ----------------------------------------------------------
    # MÉTHODE 1 : Ajouter un dataset
    # ----------------------------------------------------------
    def ajouter_dataset(self, dataset):
        """
        Ajoute un objet Dataset à la liste interne.

        Paramètre :
        -----------
        dataset : Dataset → l'objet à ajouter

        On pourrait aussi vérifier ici qu'il n'existe pas déjà (même id).
        """
        self.datasets.append(dataset)  # append() ajoute en fin de liste
        print(f"  ✅ Dataset '{dataset.nom}' [{dataset.id_dataset}] ajouté avec succès.")

    # ----------------------------------------------------------
    # MÉTHODE 2 : Afficher tous les datasets
    # ----------------------------------------------------------
    def afficher_datasets(self):
        """
        Parcourt la liste et affiche les infos de chaque dataset.
        Si la liste est vide, affiche un message d'avertissement.
        """
        if not self.datasets:   # 'not []' est True → liste vide
            print("  ⚠ Aucun dataset enregistré.")
            return

        print(f"\n{'='*45}")
        print(f"   LISTE DES DATASETS ({len(self.datasets)} au total)")
        print(f"{'='*45}")
        # On boucle sur chaque dataset avec enumerate pour avoir le numéro
        for i, ds in enumerate(self.datasets, start=1):
            print(f"\n  [{i}]", end="")
            ds.afficher_infos()

    # ----------------------------------------------------------
    # MÉTHODE 3 : Rechercher un dataset par son id
    # ----------------------------------------------------------
    def rechercher_par_id(self, id_dataset):
        """
        Recherche et retourne un dataset par son identifiant.

        Paramètre :
        -----------
        id_dataset : str → l'identifiant à chercher

        Retourne :
        ----------
        Dataset → l'objet trouvé

        Lève :
        ------
        DatasetIntrouvableException → si aucun dataset ne correspond
        """
        # On parcourt la liste et on cherche l'id correspondant
        for ds in self.datasets:
            if ds.id_dataset == id_dataset:
                return ds   # Trouvé ! On retourne l'objet immédiatement

        # Si on arrive ici, c'est que la boucle n'a rien trouvé
        raise DatasetIntrouvableException(
            f"Aucun dataset avec l'ID '{id_dataset}' n'a été trouvé."
        )

    # ----------------------------------------------------------
    # MÉTHODE 4 : Supprimer un dataset par son id
    # ----------------------------------------------------------
    def supprimer_dataset(self, id_dataset):
        """
        Recherche un dataset par son id et le supprime de la liste.

        On réutilise rechercher_par_id() pour éviter de dupliquer
        la logique de recherche (principe DRY : Don't Repeat Yourself).

        Lève DatasetIntrouvableException si l'id n'existe pas.
        """
        ds = self.rechercher_par_id(id_dataset)   # peut lever l'exception
        self.datasets.remove(ds)                   # remove() supprime l'objet
        print(f"  ✅ Dataset '{ds.nom}' [{id_dataset}] supprimé avec succès.")

    # ----------------------------------------------------------
    # MÉTHODE 5 : Filtrer les datasets par type
    # ----------------------------------------------------------
    def filtrer_par_type(self, type_donnees):
        """
        Retourne la liste des datasets dont le type correspond.

        Paramètre :
        -----------
        type_donnees : str → ex: "CSV", "JSON", "LOG"

        Retourne :
        ----------
        list → sous-liste des datasets correspondants (peut être vide)

        On utilise une 'list comprehension' :
            [element for element in liste if condition]
        C'est une façon Python élégante et courte de filtrer une liste.
        """
        type_donnees = type_donnees.upper()   # Normalisation en majuscules
        resultats = [ds for ds in self.datasets if ds.type_donnees == type_donnees]

        if not resultats:
            print(f"  ⚠ Aucun dataset de type '{type_donnees}' trouvé.")
        else:
            print(f"\n  Datasets de type '{type_donnees}' ({len(resultats)} trouvé(s)) :")
            for ds in resultats:
                ds.afficher_infos()

        return resultats

    # ----------------------------------------------------------
    # MÉTHODE 6 : Calculer la taille totale
    # ----------------------------------------------------------
    def calculer_taille_totale(self):
        """
        Calcule et retourne la somme des tailles de tous les datasets.

        On utilise la fonction built-in sum() avec une generator expression
        pour additionner tous les taille_mo en une seule ligne.

        Retourne :
        ----------
        float → taille totale en Mo
        """
        total = sum(ds.taille_mo for ds in self.datasets)
        print(f"\n  📊 Taille totale de tous les datasets : {total:.2f} Mo")
        # Le :.2f formate le float avec exactement 2 décimales (ex: 1234.50 Mo)
        return total

    # ----------------------------------------------------------
    # MÉTHODE 7 : Afficher uniquement les datasets volumineux
    # ----------------------------------------------------------
    def afficher_datasets_volumineux(self):
        """
        Filtre et affiche les datasets dont la taille dépasse 1000 Mo.

        On utilise la méthode est_volumineux() de Dataset
        pour ne pas répéter la règle métier (> 1000 Mo) ici.
        """
        volumineux = [ds for ds in self.datasets if ds.est_volumineux()]

        if not volumineux:
            print("  ✓ Aucun dataset volumineux (tous < 1000 Mo).")
        else:
            print(f"\n  ⚠ Datasets volumineux ({len(volumineux)} trouvé(s)) :")
            for ds in volumineux:
                ds.afficher_infos()

        return volumineux
