from config.database import get_connection

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
        )
        """)
        
        conn.commit()
        base.close()
        conn.close()
        
    @staticmethod
    def get_all():
        conn = get_connection()
        base = conn.cursor()
    
        base.execute("SELECT id, firstName, lastName FROM tutors")
        tutors = base.fetchall()
        
        base.close()
        conn.close()
            
        return tutors