from models import Producto
from database import SessionLocal


def create_product(nombre: str, descripcion: str, categoria: str, precio: float, stock: int):

    db = SessionLocal()
    try:
        new_product = Producto(
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
            precio=precio,
            stock=stock)
        
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    finally:
        db.close()






def get_product_by_category(categoria: str):
    db = SessionLocal()
    try:
        products = db.query(Producto).filter(Producto.categoria == categoria).all()
        return products
    finally:
        db.close()







def delete_product(id: int):
    db = SessionLocal()
    try:
        product = db.query(Producto).filter(Producto.id == id).first()
        if product != None:
            db.delete(product)
            db.commit()
            print(f"El producto con id {id}, {product.nombre} de la categoria {product.categoria} fue eliminado con exito!!!")
        else:
            print("Producto no encontrado.")
    finally:
        db.close




def update_product(id: int, nombre_actualizar: str, descripcion_actualizar: str, categoria_actualizar: str, precio_actualizar: float, stock_actualizar: int):
    db = SessionLocal()
    try:
        product = db.query(Producto).filter(Producto.id == id).first()
        if product != None:
            product.nombre = nombre_actualizar,
            product.descripcion = descripcion_actualizar,
            product.categoria = categoria_actualizar,
            product.precio = precio_actualizar,
            product.stock = stock_actualizar
            
            db.commit()
            db.refresh(product)
        
        else:
            print("El producto ingresado no se encuentra.")
        
    finally:
        db.close
        

