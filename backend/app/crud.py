from models import Producto
from database import SessionLocal

def create_product(nombre: str, descripcion: str, precio: float, stock: int):

    db = SessionLocal()
    try:
        new_product = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock)
        
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    finally:
        db.close()

# TESTING THE FUNCTION (CREATE)
#producto_creado = create_product(
    nombre="Laptop",
    descripcion="Laptop de alta gama",
    precio=1500.00,
    stock=10
#)
#print(f"Producto creado: {producto_creado.nombre} con ID {producto_creado.id}")