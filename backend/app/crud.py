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
        


# TESTING THE FUNCTION (CREATE)
producto_creado = create_product(
    nombre="Estufa",
    descripcion="Estufa electrica",
    categoria="Electrodomesticos",
    precio=1500.00,
    stock=50
)
print(f"Producto creado: {producto_creado.nombre} con ID {producto_creado.id}")



# TESTING THE FUNCTION (GET)

products = get_product_by_category("Electrodomesticos")

for p in products:
    print(p.id, p.nombre, p.descripcion, p.categoria)




# TESTING THE FUNCTION (DELETE)

product_eliminar = delete_product(2, Producto.nombre, Producto.categoria)



# TESTING THE FUNCTION (UPDATE)

producto_actualizado = update_product(
    id= 1,
    nombre_actualizar = "Moto",
    descripcion_actualizar = "250CC",
    categoria_actualizar = "Vehiculo",
    precio_actualizar = 10000000,
    stock_actualizar = 1
)
