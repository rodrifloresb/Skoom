import mysql.connector

def get_connection():

    return mysql.connector.connect(
            user = 'appuser',
            password = 'apppass',
            host = 'localhost',
            port = 3307,
            database = 'appdb'
        )
    