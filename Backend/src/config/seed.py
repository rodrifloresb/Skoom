import os
from config.database import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "seed.sql")

    with open(file_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    statements = sql_script.split(";")

    for stmt in statements:
        stmt = stmt.strip()
        if stmt:
            cursor.execute(stmt)

    conn.commit()
    cursor.close()
    conn.close()