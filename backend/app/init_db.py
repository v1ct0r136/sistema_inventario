from database import Base, engine
from models import Producto

try:
    Base.metadata.create_all(bind=engine)
    print("Base de datos inicializada y tablas creadas.")
except Exception as e:
    print(f"Error al inicializar la base de datos: {e}")