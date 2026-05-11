from config.database import Database 
 
 
class OperationDAO: 
 
    def ajouter(self, type_operation, montant, id_compte): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        sql = """ 
        INSERT INTO operations(type_operation, montant, id_compte) 
        VALUES (%s, %s, %s) 
        """ 
 
        cursor.execute(sql, (type_operation, montant, id_compte)) 
        connection.commit() 
 
        cursor.close() 
        connection.close() 
 
    def lister_par_compte(self, id_compte): 
        connection = Database.get_connection() 
        cursor = connection.cursor() 
 
        sql = """ 
        SELECT id_operation, type_operation, montant, date_operation 
        FROM operations 
        WHERE id_compte = %s 
        ORDER BY date_operation DESC 
        """ 
 
        cursor.execute(sql, (id_compte,)) 
        rows = cursor.fetchall() 
 
        cursor.close() 
        connection.close() 
 
        return rows