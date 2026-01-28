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
            course VARCHAR(50)
        );
        """)
        
    @staticmethod
    @db_handler
    def get_all(cursor):
        cursor.execute("SELECT id, firstName, lastName, tuition FROM students;")
        return cursor.fetchall()
    
    @staticmethod
    @db_handler
    def get_by(cursor, field: str, value):
        fields = {"id", "firstName", "lastName","course"}
        
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        query = f"""
            SELECT id, firstName, lastName, tuition FROM students
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
        course
        ):
        
        cursor.execute(
            """
                INSERT INTO students (firstName, lastName, tuiton, course)
                VALUES(%s, %s, %s, %s);         
            """, (firstName, lastName, tuition, course)
        )
        
    @staticmethod
    @db_handler
    def delete(cursor, id):
        cursor.execute("DELETE FROM students WHERE id = %s;" (id,))
        
    @staticmethod
    @db_handler
    def update(cursor, id, field: str, value):
        
        fields = {"firstName","lastName", "course"}
                
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        
        cursor.execute(f"UPDATE students SET {field} = %s WHERE id = %s", (value, id,))

        if cursor.rowcount == 0:
            raise ValueError("Estudiante no encontrado")
        