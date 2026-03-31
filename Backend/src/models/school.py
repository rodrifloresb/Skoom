from utils.db_handler import db_handler

class School:

    @staticmethod
    @db_handler
    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS schools(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            mail VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            phoneNumber VARCHAR(20) NOT NULL,
            address VARCHAR(255) NOT NULL,
            logo INT
        );
        """)

    @staticmethod
    @db_handler
    def get_all(cursor):
        cursor.execute("SELECT id, name, mail FROM schools;")
        return cursor.fetchall()

    @staticmethod
    @db_handler
    def get_by(cursor, field: str, value):
        fields = {"id", "name", "mail", "password", "phoneNumber", "address", "logo"}

        if field not in fields:
            raise ValueError("Campo no permitido")

        query = f"""
            SELECT id, name, mail, phoneNumber, address
            FROM schools
            WHERE {field} = %s;
        """

        cursor.execute(query, (value,))
        return cursor.fetchall()

    @staticmethod
    @db_handler
    def create(cursor, name, mail, password, phoneNumber, address):
        cursor.execute(
            """INSERT INTO schools (name, mail, password, phoneNumber, address) 
            VALUES (%s, %s, %s, %s, %s);""",
            (name, mail, password, phoneNumber, address)
        )

        return cursor.fetchall()

    @staticmethod
    @db_handler
    def delete(cursor, id):
        cursor.execute("DELETE FROM schools WHERE id = %s;", (id,))

    @staticmethod
    @db_handler
    def update(cursor, id, field: str, value):
        fields = {"name", "mail", "password", "phoneNumber", "address", "logo"}

        if field not in fields:
            raise ValueError("Campo no permitido")

        cursor.execute(f"UPDATE schools SET {field} = %s WHERE id = %s", (value, id,))

        if cursor.rowcount == 0:
            raise ValueError("School no encontrado")
        
        return cursor.fetchall()