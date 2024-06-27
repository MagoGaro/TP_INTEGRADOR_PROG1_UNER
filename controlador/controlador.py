import json

def ruta_archivo(nombre):
    return  './ddbb/' + nombre + '.json'

def leer_archivo(nombre):
    ruta = ruta_archivo(nombre)
    with open(ruta, 'r', encoding='utf-8') as f:
        carga = f.read()

    contenido = json.loads(carga)

    return contenido

def incrementar_id(nombre, tipo):
    ruta = ruta_archivo(nombre)
    id = leer_archivo(nombre)
    
    if tipo == 'cliente':
        id[0]['id_cliente'] += 1
        with open(ruta, 'w') as f:
            json.dump(id, f, indent=4)
        return id[0]['id_cliente']
    elif tipo == 'vehiculo':
        id[0]['id_vehiculo'] += 1
        with open(ruta, 'w') as f:
            json.dump(id, f, indent=4)
        return id[0]['id_vehiculo']
    else:
        id[0]['id_transaccion'] += 1
        with open(ruta, 'w') as f:
            json.dump(id, f, indent=4)
        return id[0]['id_transaccion']
    
