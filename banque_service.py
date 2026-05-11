from dao.utilisateur_dao import UtilisateurDAO 
from dao.compte_dao import CompteDAO 
from dao.operation_dao import OperationDAO 
from models.compte_courant import CompteCourant 
from models.compte_epargne import CompteEpargne 
from models.compte import Compte 
from exceptions.banque_exceptions import ( 
    UtilisateurIntrouvableException, CompteIntrouvableException 
) 
 
 
class BanqueService: 
 
    def __init__(self): 
        self.utilisateur_dao = UtilisateurDAO() 
        self.compte_dao = CompteDAO() 
        self.operation_dao = OperationDAO() 
 
    def creer_compte(self, id_user, type_compte, solde_initial): 
        utilisateur = self.utilisateur_dao.rechercher_par_id(id_user) 
 
        if utilisateur is None: 
            raise UtilisateurIntrouvableException("Utilisateur introuvable.") 
 
        numero = Compte.generer_numero_compte(id_user) 
 
        if type_compte == "COURANT": 
            compte = CompteCourant(numero, solde_initial, id_user) 
        elif type_compte == "EPARGNE": 
            compte = CompteEpargne(numero, solde_initial, id_user) 
        else: 
            raise ValueError("Type de compte invalide.") 
 
        self.compte_dao.ajouter(compte, type_compte) 
 
    def deposer(self, id_compte, montant): 
        compte = self.compte_dao.rechercher_par_id(id_compte) 
 
        if compte is None: 
            raise CompteIntrouvableException("Compte introuvable.") 
 
        compte.deposer(montant) 
        self.compte_dao.mettre_a_jour_solde(id_compte, compte.get_solde()) 
        self.operation_dao.ajouter("DEPOT", montant, id_compte) 
 
    def retirer(self, id_compte, montant): 
        compte = self.compte_dao.rechercher_par_id(id_compte) 
 
        if compte is None: 
            raise CompteIntrouvableException("Compte introuvable.") 
 
        compte.retirer(montant) 
        self.compte_dao.mettre_a_jour_solde(id_compte, compte.get_solde()) 
        self.operation_dao.ajouter("RETRAIT", montant, id_compte) 
 
    def afficher_comptes_utilisateur(self, id_user): 
        return self.compte_dao.lister_par_utilisateur(id_user) 
 
    def afficher_historique(self, id_compte): 
        return self.operation_dao.lister_par_compte(id_compte)