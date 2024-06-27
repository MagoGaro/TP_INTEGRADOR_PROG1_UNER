import json

def leer_archivo(nombre):
    ruta = './ddbb/' + nombre + '.json'
    with open(ruta, 'r', encoding='utf-8') as f:
        carga = f.read()

    contenido = json.loads(carga)

    return contenido