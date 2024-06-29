from .controlador import ruta_archivo,leer_archivo, incrementar_id
import json

def leer_transacciones(nombre):
    return leer_archivo(nombre)

def guardar_transacciones(transaccion,archivo):
    ruta = ruta_archivo(archivo)
    info = leer_transacciones(archivo)
    transaccion['id_transaccion'] =  incrementar_id('ids', 'transaccion')
    info.append(transaccion)

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def editar_transacciones(transaccion,archivo,id):
    ruta = ruta_archivo(archivo)
    info = leer_transacciones(archivo)

    for p in info:
        if  p['id_transaccion'] == id:
            p["tipo_transaccion"] = transaccion['tipo_transaccion']
            p["fecha"] = transaccion['fecha']
            p["monto"] = transaccion['monto']
            p["observaciones"] = transaccion['observaciones']
           
    with open(transaccion, 'w') as f:
        json.dump(info, f, indent=4)

def eliminar_transaccion(archivo,id):
    ruta = ruta_archivo(archivo)
    info = leer_transacciones(archivo)
    borrar = None
    for i, dato in enumerate(info):
        if dato['id_transaccion'] == id:
            borrar = i
            break

    del info[borrar]
    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def buscar_transaccion(archivo, mail):
    info = leer_transacciones(archivo)

    transaccion = None
    for i in info:
        if i['correo_electronico'] == mail:
            transaccion = i
            break

    return transaccion
