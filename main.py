from models.utilisateur import Utilisateur 
from dao.utilisateur_dao import UtilisateurDAO 
from services.banque_service import BanqueService 
from exceptions.banque_exceptions import ( 
    MontantInvalideException, 
    SoldeInsuffisantException, 
    CompteIntrouvableException, 
    UtilisateurIntrouvableException 
) 
 
 
utilisateur_dao = UtilisateurDAO() 
banque_service = BanqueService() 
 
 
def menu(): 
    print("\n===== APPLICATION DE GESTION BANCAIRE =====") 
    print("1. Ajouter un utilisateur") 
    print("2. Lister les utilisateurs") 
    print("3. Créer un compte") 
    print("4. Afficher les comptes d’un utilisateur") 
    print("5. Faire un dépôt") 
    print("6. Faire un retrait") 
    print("7. Afficher l’historique d’un compte") 
    print("0. Quitter") 
 
 
while True: 
    menu() 
    choix = input("Votre choix : ") 
 
    try: 
        if choix == "1": 
            nom = input("Nom : ") 
            prenom = input("Prénom : ") 
            email = input("Email : ") 
            telephone = input("Téléphone : ") 
 
            utilisateur = Utilisateur(nom, prenom, email, telephone) 
            utilisateur_dao.ajouter(utilisateur) 
 
            print("Utilisateur ajouté avec succès.") 
 
        elif choix == "2": 
            utilisateurs = utilisateur_dao.lister() 
 
            for utilisateur in utilisateurs: 
                print(utilisateur.afficher_infos()) 
 
        elif choix == "3": 
            id_user = int(input("ID utilisateur : ")) 
            type_compte = input("Type de compte COURANT/EPARGNE : ").upper() 
            solde_initial = float(input("Solde initial : ")) 
 
            banque_service.creer_compte(id_user, type_compte, solde_initial) 
 
            print("Compte créé avec succès.") 
 
        elif choix == "4": 
            id_user = int(input("ID utilisateur : ")) 
 
            comptes = banque_service.afficher_comptes_utilisateur(id_user) 
 
            for compte in comptes: 
                print(compte.afficher_infos()) 
 
        elif choix == "5": 
            id_compte = int(input("ID compte : ")) 
            montant = float(input("Montant à déposer : ")) 
 
            banque_service.deposer(id_compte, montant) 
 
            print("Dépôt effectué avec succès.") 
 
        elif choix == "6": 
            id_compte = int(input("ID compte : ")) 
            montant = float(input("Montant à retirer : ")) 
 
            banque_service.retirer(id_compte, montant) 
 
            print("Retrait effectué avec succès.") 
 
        elif choix == "7": 
            id_compte = int(input("ID compte : ")) 
 
            operations = banque_service.afficher_historique(id_compte) 
 
            for op in operations: 
                print(f"{op[0]} | {op[1]} | {op[2]} FCFA | {op[3]}") 
 
        elif choix == "0": 
            print("Fin du programme.") 
            break 
 
        else: 
            print("Choix invalide.") 
 
    except MontantInvalideException as e: 
        print("Erreur :", e) 
 
    except SoldeInsuffisantException as e: 
        print("Erreur :", e) 
 
    except CompteIntrouvableException as e: 
        print("Erreur :", e) 
 
    except UtilisateurIntrouvableException as e: 
        print("Erreur :", e) 
 
    except ValueError as e: 
        print("Erreur de saisie :", e) 
 
    except Exception as e: 
        print("Erreur inattendue :", e)