class Utilisateur: 
    def __init__(self, nom, prenom, email, telephone=None, id_user=None): 
        self.__id_user = id_user 
        self.__nom = nom 
        self.__prenom = prenom 
        self.__email = email 
        self.__telephone = telephone 
    def get_id_user(self): 
        return self.__id_user 
 
    def get_nom(self): 
        return self.__nom 
 
    def set_nom(self, nom): 
        if not nom: 
            raise ValueError("Le nom ne peut pas être vide.") 
        self.__nom = nom 
 
    def get_prenom(self): 
        return self.__prenom 
 
    def set_prenom(self, prenom): 
        if not prenom: 
            raise ValueError("Le prénom ne peut pas être vide.") 
        self.__prenom = prenom 
 
    def get_email(self): 
        return self.__email 
 
    def set_email(self, email): 
        if "@" not in email: 
            raise ValueError("Email invalide.") 
        self.__email = email 
 
    def get_telephone(self): 
        return self.__telephone 
 
    def set_telephone(self, telephone): 
        self.__telephone = telephone 
 
    def afficher_infos(self): 
        return f"{self.__id_user} - {self.__nom} {self.__prenom} - {self.__email}" 
 
    @staticmethod 
    def verifier_email(email): 
        return "@" in email and "." in email