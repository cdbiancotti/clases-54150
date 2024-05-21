# def suma(num1, num2):
#     return num1 + num2

# print(suma(1, 2))
# print(suma(2, 1))

# def resta(num1, num2):
#     return num1 - num2

# print(resta(1, 2))
# print(resta(2, 1))


# def resta(num1, num2):
#     return num1 - num2

# print(resta(1, 2))
# print(resta(num2=2, num1=1))


# def resta(num1, num2):
#     return num1 - num2

# print(resta(1, 2))
# print(resta(1, num2=2))
# print(resta(2, num1=1))
# print(resta(num2=2, 1))



# def devuelva_iterable(var1, var2, var3, var4, var5):
#     return var1, var2, var3, var4, var5

# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(4,3,1,5,2))
# print(devuelva_iterable(var4=4,var3=3,var1=1,var5=5,var2=2))
# print(devuelva_iterable(1,2,3,var5=5,var4=4))
# print(devuelva_iterable(var2=2,var4=4,3,1,5))
# print(devuelva_iterable(var2=2,3,4,var1=1,5))
# print(devuelva_iterable(1,2,4,var3=3))
# print(devuelva_iterable(1,2,4,var4=3))
# print(devuelva_iterable())


# def devuelva_iterable(var1=10, var2=20, var3=30, var4=40, var5=50):
#     return var1, var2, var3, var4, var5



# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(1,2,3,4))
# print(devuelva_iterable(1,2))
# print(devuelva_iterable())


# print(devuelva_iterable(15, var4=255))
# print(devuelva_iterable(var3=255))
# print(devuelva_iterable(var5='soy el cinco', var2=True))


# variable_prueba = 'pepe'

# def saludo():
#     print(variable_prueba)

# variable_prueba = 'pepe'

# saludo()

# # variable_prueba = 'pepe'






# def saludo():
#     # global variable_prueba
#     variable_prueba = 'otro gato'
#     print(variable_prueba)
#     # return variable_prueba
    

# variable_prueba = 'pepe'

# print(variable_prueba)
# saludo()
# # variable_prueba = saludo()
# print(variable_prueba)




# def actualizacion_de_dato(parametro):
#     parametro = 5

# dato = 2

# print(dato)
# actualizacion_de_dato(dato)
# print(dato)


# def actualizacion_de_dato(parametro):
#     parametro = 'tres'

# dato = 'asd'

# print(dato)
# actualizacion_de_dato(dato)
# print(dato)


# def actualizacion_de_dato(parametro):
#     parametro.append(True)

# dato = [1,2,3,'pepito']

# print(dato)
# actualizacion_de_dato(dato.copy())
# print(dato)

# '''
# # conjunto1 = {1, 'conjunto1', (1, True)}

# # Recordatorio
# # posiciones en disco |L15|L25|L14|L10|   |
# #                     |   |   |   |   |   |

# # guarda {1, 'conjunto1', (1, True)} en la posicion L15 de disco
# # conjunto1 <--- posicion del disco L15
# '''



# *args y **kwargs


# def suma(valor1, valor2, valor3=0):
#     return valor1 + valor2 + valor3


# # def suma(*args):
# #     # print(type(args))
# #     # print(args)
# #     suma = 0
# #     for valor in args:
# #         suma += valor
# #     return suma
    
# # print(suma(1,3,42,34,23,4))


# def concatenado(*args):
#     # print(type(args))
#     # print(args)
#     suma = []
#     for valor in args:
#         suma += valor
#     return suma
    
# print(suma([1,2,3],[3,42,34],[23,4]))


# print('pepe fort se fue de viaje')
# # print('pepe', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end=' ')
# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje')
# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje', sep='\n')
# # print(sep='\n', 'pepe', 'fort', 'se', 'fue', 'de', 'viaje')
# # print('pepe', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end=' ')
# # print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end='( estoy al final de mi print )')
# # print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end=' ')
# # print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', end='))))((((')



# def mostrar(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     for llave, valor in kwargs.items():
#         print(f'llave: {llave} -> valor: {valor}')
    
    
# mostrar(nombre='Pepito', apellido='Grillo')



def prueba_multiples_parametros(cadena, numero, *args, **kwargs):
    print(numero)
    print(args)
    print(kwargs)
    
prueba_multiples_parametros('numero va directo al 15',15, 26, True, -29391, 'pepito', marca='Ford', kilometros=24)