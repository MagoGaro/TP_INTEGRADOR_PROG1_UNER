from .controlador import ruta_archivo,leer_archivo, incrementar_id
import json

def leer_cliente(nombre):
    return leer_archivo(nombre)

def guardar_cliente(persona,archivo):
    ruta = ruta_archivo(archivo)
    info = leer_cliente(archivo)
    persona['id_cliente'] =  incrementar_id('ids', 'cliente')
    info.append(persona)

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def editar_cliente(persona,archivo,id):
    ruta = ruta_archivo(archivo)
    info = leer_cliente(archivo)

    for p in info:
        if p ['id_cliente'] == id:
            p["nombre"] = persona['nombre']
            p["apellido"] = persona['apellido']
            p["documento"] = persona['documento']
            p["direccion"] = persona['direccion']
            p["telefono"] = persona['telefono']
            p["correo_electronico"] = persona['correo_electronico']

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def eliminar_cliente(archivo,id):
    ruta = ruta_archivo(archivo)
    info = leer_cliente(archivo)
    borrar = None
    for i, dato in enumerate(info):
        if dato['id_cliente'] == id:
            borrar = i
            break

    del info[borrar]
    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def buscar_cliente(archivo, mail):
    info = leer_cliente(archivo)

    persona = None
    for i in info:
        if i['correo_electronico'] == mail:
            persona = i
            break

    return persona

