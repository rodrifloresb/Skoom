import mysql.connector

connection = mysql.connector.connect(
        user = 'appuser',
        password = 'apppass',
        host = 'localhost',
        port = 3307,
        database = 'appdb'
        )

Base = connection.cursor()


