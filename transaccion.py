import json, uuid


class Transaccion(json.JSONEncoder):

    def __init__(self, dni_cliente, tipo_movimiento, monto_movimiento, estado, nombre_comercio):
        self.Transaccion_id = str(uuid.uuid4())
        self.Dni_cliente = dni_cliente
        self.Tipo_movimiento = tipo_movimiento
        self.Monto_movimiento = monto_movimiento
        self.Estado = estado
        self.Nombre_comercio = nombre_comercio

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def cargar_persona(self, transaccion):
        archivo = open(f'./data/{self.Transaccion_id}.json', "w")
        archivo.write(str(transaccion.toJSON()))
        archivo.close()

    def menor_a_diezmil(self):

        if self.Monto_movimiento < 100000:

            print("El movimiento no requiere justificación")

        else:
            print("y si no lo es retorne un string con el valor")
