from config.database import Base
from sqlalchemy import Colum, Integer, String

class User(Base):
    Base.execute("") # Podemos enviar sql
    