import mysql.connector

base = None

def get_connection():
    global base

    if base : return base
    
    base = mysql.connector.connect(
            user = 'appuser',
            password = 'apppass',
            host = 'localhost',
            port = 3307,
            database = 'appdb'
        )
    