class Traitement:

    def __init__(self, id_traitement, nom_traitement, dataset):
        """
        Constructeur de la classe mère.
        Toutes les classes filles appelleront ce constructeur
        via super().__init__(...) pour ne pas répéter le code.
        """
        self.id_traitement = id_traitement     # ID unique du traitement
        self.nom_traitement = nom_traitement   # Nom du traitement
        self.dataset = dataset                 # Dataset cible (objet Dataset)

    def executer(self):
        
        raise NotImplementedError(
            "La méthode executer() doit être redéfinie dans la classe fille.")

    def __str__(self):
        return (
            f"Traitement[{self.id_traitement}] '{self.nom_traitement}' "
            f"sur Dataset '{self.dataset.nom}'"
        )


class NettoyageDonnees(Traitement):
    """
    Classe fille qui hérite de Traitement.
    Représente un traitement de nettoyage (suppression doublons,
    valeurs manquantes, corrections de format, etc.).

    La syntaxe 'class NettoyageDonnees(Traitement)' signifie :
    "NettoyageDonnees hérite de Traitement"
    """

    def __init__(self, id_traitement, nom_traitement, dataset):
        """
        Constructeur de la classe fille.

        super().__init__(...) appelle le constructeur de la CLASSE MÈRE
        pour initialiser les attributs communs (id, nom, dataset).
        On évite ainsi de réécrire du code identique.
        """
        super().__init__(id_traitement, nom_traitement, dataset)

    def executer(self):
        """
        Redéfinition de executer() pour le nettoyage.
        Cette méthode REMPLACE celle de la classe mère (polymorphisme).
        """
        print("\n" + "=" * 50)
        print(f"  TRAITEMENT : {self.nom_traitement}")
        print(f"  Dataset   : {self.dataset.nom} ({self.dataset.type_donnees})")
        print(f"  Type      : NETTOYAGE DES DONNÉES")
        print("=" * 50)
        print("   Détection des valeurs manquantes (NaN)...")
        print("   Suppression des doublons...")
        print("   Normalisation des formats de date...")
        print("   Correction des valeurs aberrantes...")
        print(f"  Nettoyage terminé sur '{self.dataset.nom}'")
        print("=" * 50)


class TransformationDonnees(Traitement):
    """
    Classe fille représentant un traitement de transformation
    (encodage, normalisation, agrégation, pivotage, etc.).
    """

    def __init__(self, id_traitement, nom_traitement, dataset):
        super().__init__(id_traitement, nom_traitement, dataset)

    def executer(self):
        """
        Redéfinition de executer() pour la transformation.
        """
        print("\n" + "=" * 50)
        print(f"  TRAITEMENT : {self.nom_traitement}")
        print(f"  Dataset   : {self.dataset.nom} ({self.dataset.type_donnees})")
        print(f"  Type      : TRANSFORMATION DES DONNÉES")
        print("=" * 50)
        print("  Encodage des variables catégorielles...")
        print("  Normalisation des variables numériques (Min-Max)...")
        print("  Agrégation des colonnes redondantes...")
        print("  Pivotage et restructuration du schéma...")
        print(f" Transformation terminée sur '{self.dataset.nom}'")
        print("=" * 50)


class AnalyseStatistique(Traitement):
    """
    Classe fille représentant une analyse statistique
    (moyennes, médianes, corrélations, distributions, etc.).
    """

    def __init__(self, id_traitement, nom_traitement, dataset):
        super().__init__(id_traitement, nom_traitement, dataset)

    def executer(self):
        """
        Redéfinition de executer() pour l'analyse statistique.
        """
        print("\n" + "=" * 50)
        print(f"  TRAITEMENT : {self.nom_traitement}")
        print(f"   Dataset   : {self.dataset.nom} ({self.dataset.type_donnees})")
        print(f"    Type      : ANALYSE STATISTIQUE")
        print("=" * 50)
        print(f"  Taille analysée      : {self.dataset.taille_mo} Mo")
        print(f"  Calcul des moyennes et médianes...")
        print(f"  Analyse des distributions...")
        print(f"  Calcul des corrélations inter-variables...")
        print(f"  Détection des outliers (méthode IQR)...")
        print(f"  Analyse terminée sur '{self.dataset.nom}'")
        print("=" * 50)
