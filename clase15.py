
# collections

# from collections import namedtuple, Counter

# Pescado = namedtuple('Pescado', ['nombre', 'especie', 'peso'])

# pescado1 = Pescado('pecesin', 'payaso', 200)
# # pescado2 = Pescado('pecesin', 'payaso')
# pescado2 = Pescado('pecesin', 'payaso',123,1213)

# print(Pescado)
# print(pescado1)
# print(pescado1.nombre)
# print(pescado1[0])
# print(pescado1._asdict())
# print(list(pescado1._asdict().items())[0])

# instancia_de_counter = Counter('abcabc123')
# print(instancia_de_counter)
# print(Counter((1,2,3,4,5,3,5,7,8,9,1,1,1,2,2)))

# datetime

# from datetime import datetime, timedelta

# dt = datetime.now()
# # print(dt)

# dt_custom = datetime(2000, 1, 1)
# print(dt_custom)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# print(dt.strftime("%A %d %B %Y %I:%M"))
# print(dt.hour)


# dt1 = dt.replace(day=5)
# print(dt)
# print(dt1)

# td = timedelta(days=365)
# print(td)
# dato_de_fecha_aumentado = dt + td
# dato_de_fecha_reducido = dt - td
# print(dato_de_fecha_aumentado)
# print(dt)
# print(dato_de_fecha_reducido)


# math

# import math

# print(math.pi)
# print(math.sqrt(64))
# print(round(3.3))
# print(round(3.5))
# print(round(3.8))
# print(math.floor(3.8))
# print(math.ceil(3.3))

# import random

# print(random.randrange(15))
# print(random.randrange(15, 22))
# print(random.randrange(15, 28, 2))

# lista = ['hoy', 'corri', '4', 'kilometros']
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choices(lista, k=3))
# print(random.choices(lista, k=2))
# print(random.choices(lista, k=5))
# print(random.choices(lista))


#################################################
#################################################

# nombre = input('Ingrese un nombre: ')

# print(nombre)

# archivo_abierto = open('prueba/archivo_de_prueba22.txt', 'w')

# archivo_abierto.write(nombre)

# archivo_abierto.close()


#################################################
#################################################


# datos_persona = {
#     'nombre': input('Ingrese un nombre: '),
#     'apellido': input('Ingrese un apellido: '),
#     'edad': input('Ingrese un edad: ')
# }

# archivo_abierto = open('prueba/archivo_de_prueba22.txt', 'w')

# archivo_abierto.write(f'Datos de {datos_persona["nombre"]} {datos_persona["apellido"]} con edad {datos_persona["edad"]}\n')
# archivo_abierto.write('Datos de Ricardo Fort con edad 60')
# archivo_abierto.write('''Soy la primer linea
# Soy la segunda
# Soy la tercera''')

# archivo_abierto.close()


#################################################
#################################################



# nombre = input('Ingrese un nombre: ')

# print(nombre)

# archivo_abierto = open('archivo_de_prueba.txt', 'w')

# archivo_abierto.write(nombre)

# archivo_abierto.close()

# archivo_abierto = open('archivo_de_prueba.txt', 'r')

# valor_del_archivo = archivo_abierto.read()

# print(valor_del_archivo)

# archivo_abierto.close()

# #################################################
# #################################################


# archivo_abierto = open('archivo_de_prueba.txt', 'r')

# # valor_del_archivo = archivo_abierto.read()

# # print(valor_del_archivo)
# # # print([valor_del_archivo])

# # valor_del_archivo_segunda_lectura = archivo_abierto.read()
# # print(valor_del_archivo_segunda_lectura)


# # linea1 = archivo_abierto.readline()
# # linea2 = archivo_abierto.readline()
# # linea3 = archivo_abierto.readline(10)

# # print(linea1)
# # print(linea2)
# # print(linea3)

# lineas = archivo_abierto.readlines()

# print(lineas)

# archivo_abierto.close()


#################################################
#################################################


# archivo_abierto = open('archivo_de_prueba.txt', 'r')

# valor_del_archivo = archivo_abierto.read()

# print(valor_del_archivo)
# print('#################################################')
# print(valor_del_archivo)
# print('#################################################')
# print(archivo_abierto.read())
# print('#################################################')
# archivo_abierto.seek(5)
# print(archivo_abierto.read())
# print('#################################################')

# archivo_abierto.close()

#################################################
#################################################


# nombre = input('Ingrese un nombre: ')

# print(nombre)

# archivo_abierto = open('archivo_de_prueba.txt', 'a')

# archivo_abierto.write('\n' + nombre)

# archivo_abierto.close()

#################################################
#################################################

# import json

# dicc = {
#     'key1': 'valor1',
#     'key2': True,
#     'key3': None,
#     'key4': ('valor', 123),
# }

# with open('archivo_de_no_json.json', 'w') as archivo_abierto:
#     json.dump(dicc, archivo_abierto, indent=4)
    
    
# with open('archivo_de_no_json.json', 'r') as archivo_abierto:
#     datos = json.load(archivo_abierto)
#     print(datos)
    
# print('#################################################')
# print(datos)