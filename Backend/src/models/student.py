from utils.db_handler import db_handler

class Student:

    @staticmethod
    @db_handler
    def create_table(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INT PRIMARY KEY AUTO_INCREMENT,
            firstName VARCHAR(50) NOT NULL,
            lastName VARCHAR(50) NOT NULL,
            tuition INT UNIQUE,
            course VARCHAR(50),
            tutor_id INT NOT NULL,
            colegio_id INT NOT NULL,
            
            FOREIGN KEY (tutor_id) REFERENCES tutors(id),
            FOREIGN KEY (colegio_id) REFERENCES colegios(id)
        );
        """)
        
    @staticmethod
    @db_handler
    def get_all(cursor):
        cursor.execute("SELECT id, firstName, lastName, course, tutor_id, colegio_id FROM students;")
        return cursor.fetchall()
    
    @staticmethod
    @db_handler
    def get_by(cursor, field: str, value):
        fields = {"id", "firstName", "lastName","tuition","course","tutor_id","colegio_id"}
        
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        query = f"""
            SELECT id, firstName, lastName, course, tuition, tutor_id, colegio_id
            FROM students
            WHERE {field} = %s;
        """
        
        cursor.execute(query, (value,))
        
        return cursor.fetchall()
    
    @staticmethod
    @db_handler
    def create(cursor,
        firstName,
        lastName,
        tuition,
        course,
        tutor_id,
        colegio_id
        ):
        
        cursor.execute(
            """INSERT INTO students (firstName, lastName, tuition, course, tutor_id, colegio_id)
                VALUES(%s, %s, %s, %s, %s, %s);""", 
                (firstName, lastName, tuition, course, tutor_id, colegio_id)
        )
        
        return cursor.lastrowid # Devuelve el ultimo id creado
        
    @staticmethod
    @db_handler
    def delete(cursor, id):
        cursor.execute("DELETE FROM students WHERE id = %s;", (id,))
        
    @staticmethod
    @db_handler
    def update(cursor, id, field: str, value):
        
        fields = {"firstName","lastName", "course", "tutor_id", "colegio_id"}
                
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        
        cursor.execute(f"UPDATE students SET {field} = %s WHERE id = %s", (value, id,))

        if cursor.rowcount == 0:
            raise ValueError("Estudiante no encontrado")
        