from .controlador import ruta_archivo, leer_archivo, incrementar_id
import json

def leer_vehiculo(nombre):
    return leer_archivo(nombre)

def guardar_vehiculo(auto, archivo):
    ruta = ruta_archivo(archivo)
    info = leer_vehiculo(archivo)
    auto['id_vehiculo'] = incrementar_id('ids', 'vehiculo')
    info.append(auto)

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def editar_vehiculo(auto, archivo, id):
    ruta = ruta_archivo(archivo)
    info = leer_vehiculo(archivo)

    for p in info:
        if p ['id_vehiculo'] == id:
            p["marca"] = auto['marca']
            p["modelo"] = auto['modelo']
            p["tipo"] = auto['tipo']
            p["patente"] = auto['patente']
            p["año"] = auto['año']
            p["precio_compra"] = auto['precio_compra']
            p["precio_venta"] = auto['precio_venta']
    
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
        
def buscar_auto(archivo, patente):
    info = leer_vehiculo(archivo)

    auto = None
    for i in info:
        if i['patente'] == patente:
            auto = i
            break

    return auto