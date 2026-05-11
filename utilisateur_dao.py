from config.database import Database 
from models.utilisateur import Utilisateur 
 
 
class UtilisateurDAO: 
 
    def ajouter(self, utilisateur): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        sql = """ 
        INSERT INTO utilisateurs(nom, prenom, email, telephone) 
        VALUES (%s, %s, %s, %s) 
        """ 
 
        values = ( 
            utilisateur.get_nom(), 
            utilisateur.get_prenom(), 
            utilisateur.get_email(), 
            utilisateur.get_telephone() 
        ) 
 
        cursor.execute(sql, values) 
        connection.commit() 
 
        cursor.close() 
        connection.close() 
 
    def lister(self): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        cursor.execute("SELECT id_user, nom, prenom, email, telephone FROM utilisateurs") 
        rows = cursor.fetchall() 
 
        utilisateurs = [] 
 
        for row in rows: 
            utilisateur = Utilisateur( 
                id_user=row[0], 
                nom=row[1], 
                prenom=row[2], 
                email=row[3], 
                telephone=row[4] 
            ) 
            utilisateurs.append(utilisateur) 
 
        cursor.close() 
        connection.close() 
 
        return utilisateurs 
 
    def rechercher_par_id(self, id_user): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        cursor.execute( 
            "SELECT id_user, nom, prenom, email, telephone FROM utilisateurs WHERE id_user = %s", 
            (id_user,) 
        ) 
 
        row = cursor.fetchone() 
 
        cursor.close() 
        connection.close() 
 
        if row is None: 
            return None 
 
        return Utilisateur( 
            id_user=row[0], 
            nom=row[1], 
            prenom=row[2], 
            email=row[3], 
            telephone=row[4] 
        ) 
 
    def supprimer(self, id_user): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        cursor.execute("DELETE FROM utilisateurs WHERE id_user = %s", (id_user,)) 
        connection.commit() 
 
        cursor.close() 
        connection.close()