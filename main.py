# =============================================================
# main.py
# Programme principal — Point d'entrée de l'application
# =============================================================
# Ce fichier :
#  1. Importe toutes les classes depuis leurs fichiers respectifs
#  2. Crée des utilisateurs et datasets d'exemple pour tester
#  3. Lance un menu interactif en console
# =============================================================

# --- Imports ---
# On importe chaque classe depuis son fichier (module)
from utilisateur import Utilisateur
from dataset import Dataset
from traitement import NettoyageDonnees, TransformationDonnees, AnalyseStatistique
from gestionnaire_dataset import GestionnaireDataset
from exceptions import (
    DatasetIntrouvableException,
    TailleDatasetInvalideException,
    TypeDatasetInvalideException
)


# =============================================================
# FONCTIONS UTILITAIRES
# =============================================================

def afficher_menu():
    """Affiche le menu principal dans la console."""
    print("\n" + "=" * 40)
    print("    MENU GESTION DATASETS")
    print("=" * 40)
    print("  1. Ajouter un dataset")
    print("  2. Afficher tous les datasets")
    print("  3. Rechercher un dataset")
    print("  4. Supprimer un dataset")
    print("  5. Filtrer par type")
    print("  6. Afficher les datasets volumineux")
    print("  7. Calculer la taille totale")
    print("  8. Lancer un traitement")
    print("  0. Quitter")
    print("=" * 40)


def saisir_utilisateur(utilisateurs):
    """
    Affiche la liste des utilisateurs disponibles et demande
    à l'opérateur d'en choisir un.

    Paramètre :
    -----------
    utilisateurs : dict → dictionnaire {id_user: Utilisateur}

    Retourne :
    ----------
    Utilisateur → l'utilisateur sélectionné, ou None si annulé
    """
    print("\n  Utilisateurs disponibles :")
    for uid, u in utilisateurs.items():
        print(f"    {uid} → {u.nom} ({u.role})")

    choix_uid = input("  Entrez l'ID de l'utilisateur propriétaire : ").strip()

    if choix_uid not in utilisateurs:
        print(f"  ⚠ Utilisateur '{choix_uid}' introuvable. Annulé.")
        return None

    return utilisateurs[choix_uid]


def option_ajouter_dataset(gestionnaire, utilisateurs):
    """
    Gère l'option 1 du menu : saisie et ajout d'un nouveau dataset.

    On capture toutes les exceptions possibles pour ne pas crasher
    l'application si l'utilisateur saisit des données invalides.
    """
    print("\n  --- AJOUT D'UN DATASET ---")
    try:
        id_dataset = input("  ID du dataset (ex: DS005)   : ").strip()
        nom = input("  Nom du dataset              : ").strip()
        source = input("  Source des données          : ").strip()

        # input() retourne toujours une chaîne → on convertit en float
        taille_mo = float(input("  Taille en Mo (ex: 250.5)    : "))

        print("  Types disponibles : CSV | JSON | SQL | IMAGE | LOG")
        type_donnees = input("  Type de données             : ").strip()

        # Sélection du propriétaire parmi les utilisateurs existants
        proprietaire = saisir_utilisateur(utilisateurs)
        if proprietaire is None:
            return   # On annule si aucun utilisateur valide n'est choisi

        # Création de l'objet Dataset (la validation s'y fait automatiquement)
        nouveau_ds = Dataset(id_dataset, nom, source, taille_mo, type_donnees, proprietaire)

        # Ajout au gestionnaire
        gestionnaire.ajouter_dataset(nouveau_ds)

    except TailleDatasetInvalideException as e:
        # Exception de taille : affiche le message et reprend le menu
        print(f"  ❌ Erreur de taille : {e}")
    except TypeDatasetInvalideException as e:
        # Exception de type
        print(f"  ❌ Erreur de type   : {e}")
    except ValueError:
        # Levée si float() reçoit quelque chose qui n'est pas un nombre
        print("  ❌ Valeur invalide : la taille doit être un nombre (ex: 150.5).")


def option_rechercher(gestionnaire):
    """Gère l'option 3 du menu : recherche par ID."""
    print("\n  --- RECHERCHE D'UN DATASET ---")
    id_dataset = input("  Entrez l'ID du dataset à rechercher : ").strip()
    try:
        ds = gestionnaire.rechercher_par_id(id_dataset)
        print("\n  ✅ Dataset trouvé :")
        ds.afficher_infos()
    except DatasetIntrouvableException as e:
        print(f"  ❌ {e}")


def option_supprimer(gestionnaire):
    """Gère l'option 4 du menu : suppression par ID."""
    print("\n  --- SUPPRESSION D'UN DATASET ---")
    id_dataset = input("  Entrez l'ID du dataset à supprimer : ").strip()
    try:
        gestionnaire.supprimer_dataset(id_dataset)
    except DatasetIntrouvableException as e:
        print(f"  ❌ {e}")


def option_filtrer(gestionnaire):
    """Gère l'option 5 du menu : filtrage par type."""
    print("\n  --- FILTRAGE PAR TYPE ---")
    print("  Types disponibles : CSV | JSON | SQL | IMAGE | LOG")
    type_donnees = input("  Entrez le type à filtrer : ").strip()
    gestionnaire.filtrer_par_type(type_donnees)


def option_lancer_traitement(gestionnaire):
    """
    Gère l'option 8 du menu : lancement d'un traitement.

    L'utilisateur choisit un dataset et un type de traitement,
    puis le traitement est instancié et executé.
    """
    print("\n  --- LANCEMENT D'UN TRAITEMENT ---")

    if not gestionnaire.datasets:
        print("  ⚠ Aucun dataset disponible. Ajoutez-en d'abord.")
        return

    # Afficher les datasets disponibles
    print("\n  Datasets disponibles :")
    for ds in gestionnaire.datasets:
        print(f"    {ds.id_dataset} → {ds.nom} ({ds.type_donnees}, {ds.taille_mo} Mo)")

    id_dataset = input("\n  ID du dataset à traiter : ").strip()

    try:
        ds_cible = gestionnaire.rechercher_par_id(id_dataset)
    except DatasetIntrouvableException as e:
        print(f"  ❌ {e}")
        return

    # Choix du type de traitement
    print("\n  Types de traitement :")
    print("    1. Nettoyage des données")
    print("    2. Transformation des données")
    print("    3. Analyse statistique")

    choix_traitement = input("  Votre choix (1/2/3) : ").strip()

    id_t = input("  ID du traitement (ex: T001) : ").strip()
    nom_t = input("  Nom du traitement           : ").strip()

    # Instanciation de la bonne classe fille selon le choix
    # C'est ici que le POLYMORPHISME agit :
    # peu importe la classe choisie, on appelle toujours .executer()
    if choix_traitement == "1":
        traitement = NettoyageDonnees(id_t, nom_t, ds_cible)
    elif choix_traitement == "2":
        traitement = TransformationDonnees(id_t, nom_t, ds_cible)
    elif choix_traitement == "3":
        traitement = AnalyseStatistique(id_t, nom_t, ds_cible)
    else:
        print("  ❌ Choix invalide.")
        return

    # Exécution du traitement (polymorphisme : chaque classe a sa propre version)
    traitement.executer()


# =============================================================
# PROGRAMME PRINCIPAL
# =============================================================

def main():
    """
    Fonction principale : initialise l'application et lance le menu.

    On crée d'abord quelques utilisateurs et datasets de démonstration
    pour avoir des données avec lesquelles travailler.
    """

    print("\n" + "=" * 50)
    print("  BIENVENUE DANS L'APP DE GESTION DE DATASETS")
    print("  © Licence Big Data et Base de données — ISSEA")
    print("=" * 50)

    # ----- Création des utilisateurs de démonstration -----
    # On stocke les utilisateurs dans un dictionnaire {id: objet}
    # pour y accéder facilement par leur id
    utilisateurs = {}

    u1 = Utilisateur("U001", "Alice Mbarga", "alice@datasociety.cm", "Data Engineer")
    u2 = Utilisateur("U002", "Bob Nguema",  "bob@datasociety.cm",   "Data Analyst")
    u3 = Utilisateur("U003", "Clara Diouf", "clara@datasociety.cm", "DBA")

    utilisateurs[u1.id_user] = u1
    utilisateurs[u2.id_user] = u2
    utilisateurs[u3.id_user] = u3

    print("\n  ✅ 3 utilisateurs chargés :")
    for u in utilisateurs.values():
        print(f"     {u}")

    # ----- Création du gestionnaire -----
    gestionnaire = GestionnaireDataset()

    # ----- Ajout de datasets de démonstration -----
    datasets_demo = [
        Dataset("DS001", "Ventes 2024",     "PostgreSQL",  512.0,  "CSV",   u1),
        Dataset("DS002", "Logs serveurs",   "Syslog",      1500.0, "LOG",   u2),
        Dataset("DS003", "Clients API",     "REST API",    85.3,   "JSON",  u1),
        Dataset("DS004", "Images médicales","DICOM Server", 2500.0, "IMAGE", u3),
        Dataset("DS005", "Stocks BD",       "MySQL",       300.0,  "SQL",   u2),
    ]

    for ds in datasets_demo:
        gestionnaire.ajouter_dataset(ds)

    print("\n  ✅ Données de démonstration chargées. Accédez au menu ci-dessous.")

    # ----- Boucle du menu interactif -----
    # La boucle tourne indéfiniment jusqu'à ce que l'utilisateur choisisse 0
    while True:
        afficher_menu()
        choix = input("  Votre choix : ").strip()

        if choix == "1":
            option_ajouter_dataset(gestionnaire, utilisateurs)

        elif choix == "2":
            gestionnaire.afficher_datasets()

        elif choix == "3":
            option_rechercher(gestionnaire)

        elif choix == "4":
            option_supprimer(gestionnaire)

        elif choix == "5":
            option_filtrer(gestionnaire)

        elif choix == "6":
            gestionnaire.afficher_datasets_volumineux()

        elif choix == "7":
            gestionnaire.calculer_taille_totale()

        elif choix == "8":
            option_lancer_traitement(gestionnaire)

        elif choix == "0":
            print("\n  Au revoir ! À bientôt. 👋\n")
            break   # 'break' sort de la boucle while et termine le programme

        else:
            print("  ⚠ Choix invalide. Entrez un chiffre entre 0 et 8.")


# =============================================================
# Point d'entrée Python
# =============================================================
# Cette condition garantit que main() n'est appelée que si on
# exécute directement ce fichier (python main.py), et NON si
# ce fichier est importé depuis un autre module.
# C'est une convention fondamentale en Python.
# =============================================================

if __name__ == "__main__":
    main()
