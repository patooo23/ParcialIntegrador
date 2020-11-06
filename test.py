import json
from transaccion import Transaccion


def test_creacion_archivo():
    transaccion_a = Transaccion(45990339, "CONSUMO", 2000, "RECHAZADO", "MUSIMUNDO")
    transaccion_b = Transaccion(45990339, "CONSUMO", 2000, "APROBADO", "MUSIMUNDO")
    transaccion_c = Transaccion(30949303, "CASH_IN", 50000, "APROBADO", "PAGOFACIL")
    transaccion_a.cargar_persona(transaccion_a)
    transaccion_b.cargar_persona(transaccion_b)
    transaccion_c.cargar_persona(transaccion_c)


def test_monto_movimiento():
    transaccion_a = Transaccion(45990339, "CONSUMO", 200000, "APROBADO", "DISCO")
    transaccion_a.menor_a_diezmil()


def test_json_movimiento():
    transaccion_a = Transaccion(30949303,"CASH_IN", 500, "APROBADO", "PAGOFACIL")
    movimiento_to_dict = json.loads(transaccion_a.toJSON())
    print(movimiento_to_dict.keys())
    print(movimiento_to_dict.items())
    print(movimiento_to_dict['Tipo_movimiento'])


test_creacion_archivo()
test_monto_movimiento()
test_json_movimiento()
