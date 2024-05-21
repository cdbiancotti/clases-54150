# print('Hola mundo!')
# print(Hola mundo!)
# print('Hola mundo!)


# if True:
    
    

# print(2+2)

# ================================================================================
# ================================================================================

# lista = []

# lista.pop()

# True or 4/0

# ================================================================================
# ================================================================================

# print(2+2)
# print(2+2)
# print(2+2)
# print(2+2)
# 4/0
# print(2+2)
# print(2+2)


# {}.discard


# ================================================================================
# ================================================================================

# def dividir(a,b):
#     if b == 0:
#         return 'No se puede dividir por cero'
#     elif type(b) not in [int, float]:
#         return 'No se puede dividir por algo que no es numerico'
#     return a/b

# print(dividir(5,'a'))


# def dividir(a,b):
#     if type(b) not in [int, float] or b == 0:
#         return 'No se puede dividir porque el divisor no es corrrecto'
#     return a/b

# print(dividir(5,'a'))


# def dividir(a,b):
#     # return a/b
#     try:
#         print(2+2)
#         print(2+2)
#         print(a/b)
#         print(2+2)
#         print(2+2)
#         print(2+2)
#         return a/b
#     except:
#         return 'No se puede dividir porque el divisor no es corrrecto'

# print(dividir(5,'a'))
# # print(dividir(5,0))


# def dividir(a,b):
#     try:
#         return a/b
#     except:
#         print('No se puede dividir porque el divisor no es corrrecto')
#     return 'chinverguencha'

# try:
#     print(dividir(5,'a'))
# except:
#     print('Mensaje del except de afuera')

bandera = True
while bandera:
    print('''
Seleccione una opcion:
1. Retirar efectivo.
2. Cambiar contraseña.
3. Salir.
''')
    try:
        opcion = input('Ingrese la opcion:')
        if opcion == '1':
            print('Retirar efectivo')
        elif opcion == '2':
            print('Cambiar contraseña')
        elif opcion == '3':
            bandera = False
        else:
            raise Exception()
    except:
        print('Ingresaste algo incorrecto. Volve a seleccionar una opcion.')
    else:
        print('Pase por el else')
    finally:
        print('Pase por el finally')




# print('''
# Seleccione una opcion:
# 1. Retirar efectivo.
# 2. Cambiar contraseña.
# 3. Salir.
# ''')
# try:
#     opcion = input('Ingrese la opcion:')
#     if opcion == '1':
#         print('Retirar efectivo')
#     elif opcion == '2':
#         print('Cambiar contraseña')
#     elif opcion == '3':
#         bandera = False
#     else:
        # raise Exception()
# except:
#     print('Ingresaste algo incorrecto. Volve a seleccionar una opcion.')
# else:
#     print('Pase por el else')

# ================================================================================
# ================================================================================


# def dividir(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as error:
#         # return f'No podes dividir por cero {error}'
#         return f'No podes dividir por cero {type(error).__name__}'
#     except TypeError as pepito:
#         # return f'El tipo no es correcto {pepito}'
#         return f'El tipo no es correcto {type(pepito)}'
#     except Exception as er:
#         # return f'Pase por el except {er}'
#         return f'Pase por el except {type(er)}'
    
    
# print(dividir(5,'a'))
# print(dividir(5,0))


# # print(type(24).__name__)


# {'pepito': 'ihnfiuqefkuabcilw',
#  'ricardomiameeee': 'wibwieubwoef',}

