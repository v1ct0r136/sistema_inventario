from database import Base
from sqlalchemy import Column, Integer, String, Float


class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    categoria = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)