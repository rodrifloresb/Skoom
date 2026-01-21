from config.database import get_connection

fields = {"id", "firstName","lastName", "mail", "password", "phoneNumber", "address", "logo"}
class Tutor:
    
    @staticmethod
    def create_table():
        conn = get_connection()
        base = conn.cursor()
        
        base.execute("""
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
        
        conn.commit()
        base.close()
        
    @staticmethod
    def get_all():
        conn = get_connection()
        base = conn.cursor()
    
        base.execute("SELECT id, firstName, lastName FROM tutors;")
        tutors = base.fetchall()
        
        base.close()
            
        return tutors
    
    @staticmethod
    def get_by(field: str, value):
        
        global fields
        
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        conn = get_connection()
        base = conn.cursor()
        
        base.execute(f"SELECT id, firstName, lastName, mail, phoneNumber, address FROM tutors WHERE {field} = %s;"
                     , (value,))
        
        result = base.fetchall()
        
        base.close()
        
        return result
        
    
    @staticmethod
    def create(
        firstName,
        lastName,
        mail,
        password,
        phoneNumber,
        address
        ):
        
        conn = get_connection()
        base = conn.cursor()
        
        base.execute(
            """INSERT INTO tutors (firstName, lastName, mail, password, phoneNumber, address) 
            VALUES (%s, %s, %s, %s, %s, %s);""",
            (firstName, lastName, mail, password, phoneNumber, address)
        )
        
        conn.commit()
        base.close()
    
    @staticmethod
    def delete(id):
        conn = get_connection()
        base = conn.cursor()
        
        base.execute("DELETE FROM tutors WHERE id = %s;", (id,))
        
        conn.commit()
        base.close()
        
    @staticmethod
    def update(id, field: str, value):
        
        global fields
                
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        conn = get_connection()
        base = conn.cursor()
        
        base.execute(f"UPDATE tutors SET {field} = %s WHERE id = %s", (value, id,))
        
        conn.commit()
        base.close()
        
