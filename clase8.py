# suma = 2+3
# suma+=1
# print(suma)


# cadena = 'Hola soy el kiosquero'
# print(len(cadena))


# contador = 0
# for letra in cadena:
#     contador +=1
    
# print(contador)

# contador = 0
# for letra in cadena:
#     contador +=1
    
# print(contador)

# def nuestro_len(param1, param2, otro_parametro):
#     ... # Bloque de codigo
#     return ... # Devolucion de un valor, los puntos suspensivos representan en este caso cualquier dato

# cadena = 'Hola soy el kiosquero'
# print(len(cadena))

# def nuestro_len(valor):
#     contador = 0
#     for _ in valor:
#         contador +=1
        
#     return contador

# print(nuestro_len(cadena))

# cadena2 = 'Mira, compre una tele y no funciona'
# print(len(cadena2))

# print(nuestro_len(cadena2))

# lista = [1,2,3,4,5,6,76]
# print(len(lista))
# print(nuestro_len(lista))

# conjunto = {1,2,3,4,5,6,76}
# print(len(conjunto))
# print(nuestro_len(conjunto))

# # ejemplo extra
# def nuestro_len(datos):
#     contador = 0
#     for dato in datos:
#         contador +=1
#         if dato == 55:
#             return 'El dato es 55, no te voy a terminar de contar los elementos.'
            
#     return contador

# conjunto = {1,2,3,4,55,5,6,76}
# print(len(conjunto))
# print(nuestro_len(conjunto))


# def suma(num1, num2):
#     return num1 + num2

# print(suma(1, 2))
# print(suma(2, 1))

# def resta(num1, num2):
#     return num1 - num2

# print(resta(1, 2))
# print(resta(2, 1))


# def welcome(ciudad):
#     print(f'¡hola bienvenidx a {ciudad}!')

# welcome(input('Ingrese ciudad: '))



# valores = []

# def calcular_media(lista_de_numeros):
#     if lista_de_numeros:
#         return sum(lista_de_numeros) / len(lista_de_numeros)

# print('La media de la lista "valores" es', calcular_media(valores))



# def es_multiplo():
#     num1 = int(input('Ingresa un numero: '))
#     num2 = int(input('Ingresa otro numero: '))

#     if num1%num2==0:
#         print(f'El segundo valor "{num1}" es multiplo del primer "{num2}"')
#     elif num2%num1==0:
#         print(f'El primer valor "{num1}" es multiplo del segundo "{num2}"')
#     else:
#         print(f'{num1}, {num2} no son multiplos entre si')

# es_multiplo()


# def es_multiplo():
#     num1 = int(input('Ingresa un numero: '))
#     num2 = int(input('Ingresa otro numero: '))

#     if num1%num2==0:
#         return f'El segundo valor "{num1}" es multiplo del primer "{num2}"'
#     elif num2%num1==0:
#         return f'El primer valor "{num1}" es multiplo del segundo "{num2}"'
#     else:
#         return f'{num1}, {num2} no son multiplos entre si'

# print(es_multiplo())



# def anio_bisiesto(anio):
    
#     for caracter in anio:
#         if caracter not in '0123456789':
#             print(f'Ingresaste {anio} pero lo que debes ingresar tiene que ser un número.')
#             return
            
#     anio_numerico = int(anio)
    
#     if (
#         anio_numerico%4==0 and 
#         (anio_numerico%100==1 or 
#         anio_numerico%400==0)
#     ):
#         print(f'El año {anio} es bisiesto')
#     else:
#         print(f'El año {anio} no es bisiesto')

    

# anio_bisiesto(input('Ingrese un año: '))