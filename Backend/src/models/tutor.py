from utils.db_handler import db_handler

class Tutor:
    
    @staticmethod
    @db_handler
    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tutors(
            id INT PRIMARY KEY AUTO_INCREMENT,
            firstName VARCHAR(50) NOT NULL,
            lastName VARCHAR(50) NOT NULL,
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
        cursor.execute("SELECT id, firstName, lastName FROM tutors;")
        return cursor.fetchall()

    
    @staticmethod
    @db_handler
    def get_by(cursor, field: str, value):
        fields = {"id", "firstName","lastName", "mail", "phoneNumber", "address"}


        if field not in fields:
            raise ValueError("Campo no permitido")

        query = f"""
            SELECT *
            FROM tutors
            WHERE {field} = %s;
        """

        cursor.execute(query, (value,))
        
        return cursor.fetchall()

        
    
    @staticmethod
    @db_handler
    def create(cursor,
        firstName,
        lastName,
        mail,
        password,
        phoneNumber,
        address
        ):

        cursor.execute(
            """INSERT INTO tutors (firstName, lastName, mail, password, phoneNumber, address) 
            VALUES (%s, %s, %s, %s, %s, %s);""",
            (firstName, lastName, mail, password, phoneNumber, address)
       )
    
        return cursor.fetchall()
        
    @staticmethod
    @db_handler
    def delete(cursor, id):
        cursor.execute("DELETE FROM tutors WHERE id = %s;", (id,))
        
        return cursor.fetchall()
        
    @staticmethod
    @db_handler
    def update(cursor, id, field: str, value):
        
        fields = {"firstName","lastName", "mail", "password", "phoneNumber", "address", "logo"}
                
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        
        cursor.execute(f"UPDATE tutors SET {field} = %s WHERE id = %s", (value, id,))

        if cursor.rowcount == 0:
            raise ValueError("Tutor no encontrado")
        
        return cursor.fetchall()