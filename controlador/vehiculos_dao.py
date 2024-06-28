from .controlador import ruta_archivo, leer_archivo, incrementar_id
import json

def leer_vehiculo(nombre):
    return leer_archivo(nombre)

def guardar_vehiculo(vehiculo, archivo):
    ruta = ruta_archivo(archivo)
    info = leer_vehiculo(archivo)
    vehiculo['id_vehiculo'] = incrementar_id('ids', 'vehiculo')
    info.append(vehiculo)

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def editar_vehiculo(vehiculo, archivo, id):
    ruta = ruta_archivo(archivo)
    info = leer_vehiculo(archivo)

    for p in info:
        if p ['id_vehiculo'] == id:
            p["marca"] = vehiculo['marca']
            p["modelo"] = vehiculo['modelo']
            p["tipo"] = vehiculo['tipo']
            p["patente"] = vehiculo['patente']
            p["año"] = vehiculo['año']
            p["precio_compra"] = vehiculo['precio_compra']
            p["precio_venta"] = vehiculo['precio_venta']
    
    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def eliminar_vehiculo(archivo, id):
    ruta = ruta_archivo(archivo)
    info = leer_vehiculo(archivo)
    borrar = None
    for i, dato in enumerate(info):
        if dato['id_vehiculo'] == id:
            borrar = i
            break

    del info[borrar]
    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)
        