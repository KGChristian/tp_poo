from config.database import Database 
from models.compte_courant import CompteCourant 
from models.compte_epargne import CompteEpargne 
 
 
class CompteDAO: 
 
    def ajouter(self, compte, type_compte): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        sql = """ 
        INSERT INTO comptes(numero_compte, solde, type_compte, id_user) 
        VALUES (%s, %s, %s, %s) 
        """ 
 
        values = ( 
            compte.get_numero_compte(), 
            compte.get_solde(), 
            type_compte, 
            compte.get_id_user() 
        ) 
 
        cursor.execute(sql, values) 
        connection.commit() 
 
        cursor.close() 
        connection.close() 
 
    def lister_par_utilisateur(self, id_user): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        sql = """ 
        SELECT id_compte, numero_compte, solde, type_compte, id_user 
        FROM comptes 
        WHERE id_user = %s 
        """ 
 
        cursor.execute(sql, (id_user,)) 
        rows = cursor.fetchall() 
 
        comptes = [] 
 
        for row in rows: 
            if row[3] == "COURANT": 
                compte = CompteCourant( 
                    id_compte=row[0], 
                    numero_compte=row[1], 
                    solde=float(row[2]), 
                    id_user=row[4] 
                ) 
            else: 
                compte = CompteEpargne( 
                    id_compte=row[0], 
                    numero_compte=row[1], 
                    solde=float(row[2]), 
                    id_user=row[4] 
                ) 
 
            comptes.append(compte) 
 
        cursor.close() 
        connection.close() 
 
        return comptes 
 
    def rechercher_par_id(self, id_compte): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        sql = """ 
        SELECT id_compte, numero_compte, solde, type_compte, id_user 
        FROM comptes 
        WHERE id_compte = %s 
        """ 
 
        cursor.execute(sql, (id_compte,)) 
        row = cursor.fetchone() 
 
        cursor.close() 
        connection.close() 
 
        if row is None: 
            return None 
 
        if row[3] == "COURANT": 
            return CompteCourant( 
                id_compte=row[0], 
                numero_compte=row[1], 
                solde=float(row[2]), 
                id_user=row[4] 
            ) 
 
        return CompteEpargne( 
            id_compte=row[0], 
            numero_compte=row[1], 
            solde=float(row[2]), 
            id_user=row[4] 
        ) 
 
    def mettre_a_jour_solde(self, id_compte, nouveau_solde): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        cursor.execute( 
            "UPDATE comptes SET solde = %s WHERE id_compte = %s", 
            (nouveau_solde, id_compte) 
        ) 
 
        connection.commit() 
 
        cursor.close() 
        connection.close()