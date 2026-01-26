from functools import wraps
from mysql.connector import Error
from config.database import get_connection

def db_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            result = func(cursor, *args, **kwargs)
            conn.commit()
            return {"ok": True,"data": result}

        except Exception as e:
            conn.rollback()
            return {"ok": False,"error": str(e)}

        finally:
            cursor.close()
            conn.close()

    return wrapper
