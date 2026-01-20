from config.database import get_connection

#aca va el codigo necesario para que interactue con la bd

class Colegio:

    @staticmethod
    def create_table():
        conn = get_connection()
        base = conn.cursor()

        base.execute("""
        CREATE TABLE IF NOT EXISTS colegios(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            mail VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            phoneNumber VARCHAR(20) NOT NULL,
            address VARCHAR(255) NOT NULL,
            logo INT
        );
        """)       

        conn.commit()  #se usa cuando cambiamos datos
        base.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        base = conn.cursor()
        
        base.execute("SELECT id, name, mail FROM colegios;")
        
        colegios = base.fetchall()
        base.close()
        
        return colegios 
    
    @staticmethod
    def get_by(field: str, value):
        fields = {"id", "name", "mail", "password", "phoneNumber", "address", "logo" }
        if field not in fields:
             raise ValueError("Campo no permitido")
        
        conn = get_connection()
        base = conn.cursor()
        base.execute(f"SELECT id, name, mail, phoneNumber, address FROM colegios where {field} = %s;" , (value,))
        res = base.fetchall()
        base.close()
        return res 
    
    @staticmethod
    def create(
        name,
        mail,
        password,
        phoneNumber,
        address
        ):
        
        conn = get_connection()
        base = conn.cursor()
        
        base.execute(
            """INSERT INTO colegios (name, mail, password, phoneNumber, address) 
            VALUES (%s, %s, %s, %s, %s);""",
            (name, mail, password, phoneNumber, address)
        )
        
        conn.commit()
        base.close()
        