from mitiendapos.servicios.ticket import generar_ticket_bytes


def test_generar_ticket_bytes_contiene_tienda_y_total():
    contenido = generar_ticket_bytes("Mi Tienda", ["Leche 1200", "Pan 500"], ancho=32)

    assert b"Mi Tienda" in contenido
    assert b"Leche 1200" in contenido
    assert b"Gracias por su compra" in contenido
