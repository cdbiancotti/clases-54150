# Strings

# Método upper

# cadena1 = 'soY la pRimer cadena'
# print(cadena1)
# cadena1_en_mayusculas = cadena1.upper()
# # cadena1 = cadena1.upper()
# print(cadena1)
# print(cadena1_en_mayusculas)

# cadena1_en_minusculas = cadena1.lower()
# print(cadena1_en_minusculas)

# cadena1_en_modo_titulo = cadena1.title()
# print(cadena1_en_modo_titulo)

# cadena1_parrafo = cadena1.capitalize()
# print(cadena1_parrafo)

# ==============================================================
# ==============================================================

# cadena1 = 'soY la pRimer cadena'
# print(cadena1.count('a'))
# print(cadena1.count(' '))
# print(cadena1.count(''))


# print(cadena1.find('a'))
# print(cadena1.find(' '))
# print(cadena1.find(''))
# print(cadena1.find('z'))


# print(cadena1.rfind('a'))
# print(cadena1.rfind(' '))
# print(cadena1.rfind(''))
# print(cadena1.rfind('z'))


# cadena2 = 'segunda cadena al rescate'
# # lista = ['segunda', 'cadena', 'al', 'rescate']
# lista = cadena2.split()
# print(lista)
# lista2 = cadena2.split('a')
# print(lista2)
# lista3 = cadena2.split('a ')
# print(lista3)
# lista4 = cadena2.split('asd el pepe loco')
# print(lista4)



# # lista = ['segunda', 'cadena', 'al', 'rescate']
# tupla = ('segunda', 'cadena', 'al', 'rescate')
# # lista = ['segunda', 'cadena', 'al', 'rescate']
# # cadena = ' '.join(lista)
# # print(cadena)
# # cadena = '<><>pepito<>solito<><>'.join(lista)
# # print(cadena)
# cadena = ' -=-=- '.join(tupla)
# print(cadena)


# password = input('Ingrese un password: ')
# # print(password.strip())
# # print(password)

# print(password.strip('asd'))
# print(password)


# palabra_repetida = 'cadena pepito cadena cadena cadena'
# # palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra')
# palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra', 3)
# print(palabra_repetida)
# print(palabra_repetida_modificada)

# Lista

# lista = ['segunda', 'cadena', 'al', 'rescate']
# print(lista)
# lista.clear()
# print(lista)

# lista2 = lista + [1,2,3]
# print(lista2)
# lista += [1,2,3]
# print(lista)
# lista.extend([1,2,3])
# print(lista)



# lista = ['segunda', 'cadena', 'al', 'rescate']
# lista.insert(0, 'pepitoooooo')
# print(lista)

# lista = lista[::-1]
# lista.reverse()
# print(lista)



# lista_numeros = [5,1,2,3,4,10]
# # lista_numeros.sort()
# lista_numeros.sort(reverse=True)
# print(lista_numeros)


# lista_numeros1 = ['5','1','2','3','4','10']
# lista_numeros1.sort()
# # lista_numeros1.sort(reverse=True)
# print(lista_numeros1)


# Sets


# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor1', (1, True))
# # el primero tiene que ser un set... el segundo un iterable
# print(conjunto1.isdisjoint(iterable1))
# iterable2 = (2, 'valor2', (2, True))
# print(conjunto1.isdisjoint(iterable2))
# iterable2 = (1, 'valor2', (2, True))
# print(conjunto1.isdisjoint(iterable2))



# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor1', (1, True), 45)
# print(conjunto1.issubset(iterable1))


# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor1', (1, True), 45)
# print(conjunto1.issuperset(iterable1))



# conjunto1 = {1, 'valor1', (1, True)}
# # iterable1 = (1, 'valor2', (2, True), 45)
# iterable1 = (2, 'valor2', (2, True), 45)
# conjunto3 = conjunto1.union(iterable1)
# print(conjunto1)
# print(conjunto3)


# conjunto1 = {1, 'valor1', (1, True)}
# # iterable1 = (2, 'valor2', (2, True), 45)
# iterable1 = (2, 'valor2', (1, True), 45)
# print(conjunto1.difference(iterable1))
# print(conjunto1)


# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# print(conjunto1.intersection(iterable1))
# variable = conjunto1.intersection(iterable1)
# print(conjunto1)



# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# conjunto1.difference_update(iterable1)
# print(conjunto1)


# conjunto1 = {1, 'valor1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# conjunto1.intersection_update(iterable1)
# print(conjunto1)

    
    


# Dicts

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# valor1 = auto['motor']
# print(valor1)
# # valor2 = auto['ricardo']
# # print(valor2)
# valor3 = auto.get('ricardo', False)
# print(valor3)


# print(auto.keys())
# print(auto.values())
# print(auto.items())








# texto = '''
# Esta es la historia de dos ranitas. Ambas vivían muy felices en Japón, pero en diferentes ciudades; una vivía en Kioto y la otra en Osaka.

# Una mañana, las dos ranitas se despertaron muy aburridas y decidieron que era hora de explorar otros lugares:

# —Hoy partiré hacia Osaka —se dijo la ranita de Kioto.

# —Hoy viajaré a Kioto —se dijo la ranita de Osaka.

# Sin saberlo, las ranitas empacaron sus cosas al mismo tiempo y salieron saltando hasta el camino de la montaña que unía las dos ciudades.

# El viaje resultó ser más largo de lo planeado y por esas cosas del destino; las dos ranitas, muy agotadas, se detuvieron en la cima de la montaña.

# Al encontrarse, las dos ranitas se observaron con emoción. Luego, se saludaron y entablaron conversación. Fue así como supieron hacia donde se dirigían.

# —¡Voy a Osaka! — dijo la ranita de Kioto—. Escuché que es una ciudad esplendorosa.

# —¡Y yo voy a Kioto! — respondió la ranita de Osaka—. Todos dicen que es una ciudad espléndida.

# —Es una pena que no seamos más altas— dijo la ranita de Kioto—. Si lo fuéramos, podríamos ver desde lo alto de esta montaña la ciudad que queremos visitar.

# —¡Tengo una idea! — exclamó la ranita de Osaka—. Parémonos de puntitas con nuestras patas traseras y apoyémonos una a la otra. Así podemos echarle un vistazo a la ciudad a donde vamos.

# Entonces, las dos ranitas se pararon de puntitas y se tomaron de las patas delanteras para no caerse.

# La rana de Kioto alzó la cabeza y miró hacia Osaka. La rana de Osaka también alzó la cabeza y miró hacia Kioto

# —¡Qué decepción! — dijo la ranita de Kioto—. Osaka es igual a Kioto.

# —¡Qué desilusión! — dijo la ranita de Osaka—. Kioto es igual a Osaka.

# En ese momento, la ranita de Kioto dijo:

# —Me alegra que hayamos descubierto esto, ahora podemos ahorrarnos el largo viaje y regresar a casa.

# Las dos se despidieron y comenzaron a saltar muy felices de vuelta a sus ciudades.

# Sin embargo, las dos ranitas olvidaron que todas las ranitas del mundo tienen los ojos en la parte de arriba de la cabeza. En realidad, veían lo que estaba atrás y no adelante. ¡La ranita de Kioto estaba mirando hacia Kioto y la de Osaka estaba mirando hacia Osaka!

# '''

# texto1 = texto.replace('-', ' ')
# texto2 = texto1.replace('¡', ' ')
# texto3 = texto2.replace('.', ' ')
# texto4 = texto3.replace(',', ' ')
# texto5 = texto4.replace(':', ' ')
# texto6 = texto5.replace('!', ' ')

# lista_de_palabras = texto6.split()
# conjunto_de_palabras = set(lista_de_palabras)
# # print(conjunto_de_palabras)
# # print(len(lista_de_palabras))
# # print(len(conjunto_de_palabras))


# listado_de_caracteres = list(texto)
# conjunto_de_caracteres = set(texto)
# print(conjunto_de_caracteres)
# print(listado_de_caracteres)
# # texto6



# Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:

original = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

# Transforma el texto en:
'''
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.
'''
# Lo único prohibido es modificar directamente el texto

# v1 = original.replace('&', '.\n- ')

# # v2 = v1 + '.'
# # print(v2)

lista_de_renglones = original.split('&')
# lista_de_renglones[0] += '..'
lista_de_renglones[0] = lista_de_renglones[0].capitalize() + '..'
lista_de_renglones[1] = lista_de_renglones[1][0].upper() + lista_de_renglones[1][1:]
lista_de_renglones[2] = lista_de_renglones[2][0].upper() + lista_de_renglones[2][1:]
lista_de_renglones[3] = lista_de_renglones[3].capitalize() + '.'

print(lista_de_renglones)

v1 = '.\n- '.join(lista_de_renglones)

print(v1)