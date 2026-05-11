import pymysql


class Database: 
    @staticmethod 
    def get_connection(): 
        return pymysql.connect( 
            host="localhost", 
            user="root", 
            password="K6326gc@94", 
            database="tp_banque_poo" 
)