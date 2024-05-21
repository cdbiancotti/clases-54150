

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