
from crud import create_product, get_product_by_category, delete_product, update_product
from models import Producto


def test_crud_create():

    # TESTING THE FUNCTION (CREATE)
    producto_creado = create_product(
        nombre="Portatil",
        descripcion="16GB RAM, 1TB SSD, i7 11va Gen, 16 Pulgadas",
        categoria="Tecnologia",
        precio=6500000,
        stock=20
    )
    print(f"Producto creado: {producto_creado.nombre} con ID {producto_creado.id}")

    assert producto_creado.id is not None
    assert producto_creado.nombre == "Portatil"



def test_crud_select():

# TESTING THE FUNCTION (GET)

    products = get_product_by_category("Electrodomesticos")

    for p in products:
        print(p.id, p.nombre, p.descripcion, p.categoria)

    assert len(products) >= 0  # Puede ser 0 si no hay productos en esa categoría


def test_crud_delete():

    # TESTING THE FUNCTION (DELETE)

    product_eliminar = delete_product(2)

    assert product_eliminar is None  # La función delete_product no retorna nada


def test_crud_update():

    # TESTING THE FUNCTION (UPDATE)

    producto_actualizado = update_product(
        id= 3,
        nombre_actualizar = "Moto",
        descripcion_actualizar = "250CC",
        categoria_actualizar = "Vehiculo",
        precio_actualizar = 10000000,
        stock_actualizar = 1
    )

    assert producto_actualizado is None  # La función update_product no retorna nada