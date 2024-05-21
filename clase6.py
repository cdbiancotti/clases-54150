# esta_lloviendo = input('Esta lloviendo?? (si/no)')

# solo if
# if esta_lloviendo == 'si':
#     print('Pase por la sentencia IF')
#     print('Entonces voy a usar paraguas cuando salga.')

# print('Mi programa termino!')

# if - else
# if esta_lloviendo == 'si':
#     print('Pase por la sentencia IF')
#     print('Entonces voy a usar paraguas cuando salga.')
# else:
#     print('Pase por la sentencia IF')
#     print('Entonces no voy a usar paraguas cuando salga.')
# print('Mi programa termino!')

# if - elif - else
# if esta_lloviendo == 'si':
#     print('Entonces voy a usar paraguas cuando salga.')
# elif esta_lloviendo == 'no':
#     print('Entonces no voy a usar paraguas cuando salga.')
# else:
#     print('No entiendo que me queres decir con eso.')
# print('Mi programa termino!')


# primer_numero = 30
# if primer_numero < 20:
#     print('es menor a 20')
# elif primer_numero < 30:
#     print('es menor a 30')
# elif primer_numero < 40:
#     print('es menor a 40')
# elif primer_numero < 50:
#     print('es menor a 50')
# else:
#     print("no se cumplio nada")
    
# if primer_numero < 50:
#     print('es menor a 50')
#     if primer_numero < 40:
#         print('es menor a 40')
#         if primer_numero < 30:
#             print('es menor a 30')
#             if primer_numero < 20:
#                 print('es menor a 20')

# var = 15
# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# if primer_numero == segundo_numero:
#     print('son iguales')
#     if primer_numero < var:
#         print('son menores a var')
#     else:
#         print('son mayores a var')
# else:
#     print('no son iguales')
#     if primer_numero < var:
#         print('primer_numero es menor a var')
#         if segundo_numero < var:
#             print('segndo_numero es menor a var')
#         else:
#             print('segndo_numero es mayor a var')
#     else:
#         print('primer_numero es mayor a var')

# print('Estoy fuera de los if')


# esta_lloviendo = input('Esta lloviendo?? (si/no)')

# # v1
# pepito = ''
# if esta_lloviendo == 'si':
#     pepito = 'soy pepito'
# else:
#     pepito = 'no soy pepito :('
    
# v2
# pepito = ''
# if esta_lloviendo == 'si': pepito = 'soy pepito'

# pepito = ''
# if esta_lloviendo == 'si': pepito = 'soy pepito'
# else: pepito = 'no soy pepito :('

    
# # v3
# pepito = 'soy pepito' if esta_lloviendo == 'si' else 'no soy pepito :('

# v4
# pepito = 'soy pepito' if esta_lloviendo == 'si' else 'no soy pepito :(' if esta_lloviendo == 'no' else 'soy ricardo' 

# print(pepito)


# Actividad Marvel vs CapCom

# preferencia = input('Ingrese su preferencia: (Marvel/Capcom)').capitalize()
# nombre = input('Ingrese su nombre: ').upper()

# if preferencia == 'Marvel' and nombre < 'M' or preferencia == 'Capcom' and nombre > 'N':
#     print('Tu grupo es el A')
# else:
#     print('Tu grupo es el B')
