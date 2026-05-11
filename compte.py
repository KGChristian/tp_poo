from abc import ABC, abstractmethod 
from banque_exceptions import MontantInvalideException, SoldeInsuffisantException 
 
 
class Compte(ABC): 
    banque = "Banque Académique" 
 
    def __init__(self, numero_compte, solde, id_user, id_compte=None): 
        self.__id_compte = id_compte 
        self.__numero_compte = numero_compte 
        self.__solde = solde 
        self.__id_user = id_user 
 
    def get_id_compte(self): 
        return self.__id_compte 
 
    def get_numero_compte(self): 
        return self.__numero_compte 
 
    def get_solde(self): 
        return self.__solde 
 
    def set_solde(self, solde): 
        if solde < 0: 
            raise ValueError("Le solde ne peut pas être négatif.") 
        self.__solde = solde 
 
    def get_id_user(self): 
        return self.__id_user 
 
    def deposer(self, montant): 
        if montant <= 0: 
            raise MontantInvalideException("Le montant du dépôt doit être positif.") 
        self.__solde += montant 
 
    def retirer(self, montant): 
        if montant <= 0: 
            raise MontantInvalideException("Le montant du retrait doit être positif.") 
 
        if montant > self.__solde: 
            raise SoldeInsuffisantException("Solde insuffisant.") 
 
        self.__solde -= montant 
 
    @abstractmethod 
    def calculer_frais(self): 
        pass 
 
    @classmethod 
    def changer_banque(cls, nouveau_nom): 
        cls.banque = nouveau_nom 
 
    @staticmethod 
    def generer_numero_compte(id_user): 
        return f"CPT-{id_user}-001" 
 
    def afficher_infos(self): 
        return f"{self.__numero_compte} | Solde : {self.__solde} FCFA"