from .controlador import leer_archivo


def leer_cliente(nombre):
    return leer_archivo(nombre)



#print(leer_archivo('vehiculos'))

#x = leer_archivo('vehiculos')

#print(x[0]['patente'])