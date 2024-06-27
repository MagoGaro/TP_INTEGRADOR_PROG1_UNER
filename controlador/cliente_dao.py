from .controlador import leer_archivo, incrementar_id
import json
import base64

def leer_cliente(nombre):
    return leer_archivo(nombre)

def guardar_cliente(persona):
    ruta = './ddbb/' + 'clientes' + '.json'
    info = leer_cliente('clientes')
    persona['id_cliente'] =  incrementar_id('ids', 'cliente')
    info.append(persona)

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

#print(leer_archivo('vehiculos'))

#x = leer_archivo('vehiculos')

#print(x[0]['patente'])

