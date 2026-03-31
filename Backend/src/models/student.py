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
            tuition INT NOT NULL,
            course VARCHAR(50),
            tutor_id INT NOT NULL,
            school_id INT NOT NULL,
            
            FOREIGN KEY (tutor_id) REFERENCES tutors(id),
            FOREIGN KEY (school_id) REFERENCES schools(id),

            UNIQUE (tuition, school_id)
        );
        """)
        
        
    @staticmethod
    @db_handler
    def get_all(cursor):
        cursor.execute("SELECT id, firstName, lastName, course, tutor_id, school_id FROM students;")
        return cursor.fetchall()
    
    @staticmethod
    @db_handler
    def get_by(cursor, field: str, value):
        fields = {"id", "firstName", "lastName","tuition","course","tutor_id","school_id"}
        
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        query = f"""
            SELECT id, firstName, lastName, course, tuition, tutor_id, school_id
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
        school_id
        ):
        
        cursor.execute(
            """INSERT INTO students (firstName, lastName, tuition, course, tutor_id, school_id)
                VALUES(%s, %s, %s, %s, %s, %s);""", 
                (firstName, lastName, tuition, course, tutor_id, school_id)
        )
        
        return cursor.fetchall()
        
    @staticmethod
    @db_handler
    def delete(cursor, id):
        cursor.execute("DELETE FROM students WHERE id = %s;", (id,))
        
        return cursor.fetchall()
        
    @staticmethod
    @db_handler
    def update(cursor, id, field: str, value):
        
        fields = {"firstName","lastName", "course", "tutor_id", "school_id"}
                
        if field not in fields:
            raise ValueError("Campo no permitido")
        
        
        cursor.execute(f"UPDATE students SET {field} = %s WHERE id = %s", (value, id,))

        if cursor.rowcount == 0:
            raise ValueError("Estudiante no encontrado")
        
        return cursor.fetchall()
    
    @staticmethod
    @db_handler
    def exists(cursor, tuition, school_id):
        cursor.execute(
            "SELECT * FROM students WHERE tuition = %s AND school_id = %s;",
            (tuition, school_id)
        )
        
        return cursor.fetchone()