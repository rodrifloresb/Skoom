import mysql.connector

def get_connection():

    connection = mysql.connector.connect(
            user = 'appuser',
            password = 'apppass',
            host = 'localhost',
            port = 3307,
            database = 'appdb'
            )
    
    return connection
