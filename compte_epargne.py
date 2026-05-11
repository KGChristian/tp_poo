from models.compte import Compte 
 
 
class CompteEpargne(Compte): 
    def __init__(self, numero_compte, solde, id_user, taux_interet=0.03, id_compte=None): 
        super().__init__(numero_compte, solde, id_user, id_compte) 
        self.__taux_interet = taux_interet 
 
    def calculer_frais(self): 
        return 0 
 
    def calculer_interet(self): 
        return self.get_solde() * self.__taux_interet 
 
    def afficher_infos(self): 
        return f"[Compte Épargne] {super().afficher_infos()} | Intérêt : {self.calculer_interet()} FCFA" 