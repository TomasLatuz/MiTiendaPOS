from mitiendapos.dominio import Carro, Producto


def test_carro_agrega_y_suma_total():
    carro = Carro()
    p1 = Producto(codigo="111", nombre="Leche", precio=1200)
    p2 = Producto(codigo="222", nombre="Pan", precio=500)

    carro.agregar(p1)
    carro.agregar(p1, 2)
    carro.agregar(p2)

    assert carro.cantidad_total == 4
    assert carro.total == 1200 * 3 + 500
