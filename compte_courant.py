from models.compte import Compte 
 
 
class CompteCourant(Compte): 
    def __init__(self, numero_compte, solde, id_user, frais_tenue=1000, id_compte=None): 
        super().__init__(numero_compte, solde, id_user, id_compte) 
        self.__frais_tenue = frais_tenue 
 
    def calculer_frais(self): 
        return self.__frais_tenue 
 
    def afficher_infos(self): 
        return f"[Compte Courant] {super().afficher_infos()} | Frais : {self.__frais_tenue} FCFA" 