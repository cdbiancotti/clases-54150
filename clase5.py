# print(2+2)
# print(2*2)
# print(3-2)
# print(3**2)
# print(3/2)
# print(3//2)
# print(3%2)

# Tipo de datos logicos
# False (0)
# True (1)

# Casteado
# bool()

# print(True + 5)

# Operadores relacionales
# = es para asignacion
# == para comparar por igualdad
# < > <= >= == !=

# suma = 2 + 2
# print(2 < 2)
# print(2 > 2)
# print(2 > 4)
# print(2 < 4)
# print(2 <= 2)
# print(2 >= 2)
# print(2 <= 5)
# print(2 >= 1)
# print(1 == 1)
# print(1 != 1)
# print(suma == 4)
# print(suma == 15)
# print(suma != 4)
# print(suma != 15)


# print('a' == 'a')
# print('a' == 'A')
# print('a' != 'A')
# print('a' < 'A')
# print('a' > 'A')
# print('a'+1)

# ord()
# print(ord('a'))
# print(ord('aa'))
# chr()
# print(chr(97))


# print('ahorrar' < 'aHorrar')
# print('ah' < 'aHorrar')
# print('ah' > 'ahorrar')
# print('ah' < 'ahorraR')
# print('a' >= 'ahorrar')


# string1 = 'ricardo como ta va? soy pancho'
# palabra2 = 'hola'
# print(string1 == 'hola')
# print(string1 == palabra2)
# print(string1[0] == 'r')
# print(string1[:2] == 'r')
# print(string1[:2] == 'ri')
# # print(string1[0] * 2)

# print(1 < 'a')

# print(False * 55)
# print(True * 55)
# print(True + 55)
# print(True + 0.5)
# print(False == 0.5)
# print(False == 0)
# print(False == [])


# print(bool(-4))
# print(bool(0))
# print(bool(''))
# print(bool('123asd'))
# print(bool([]))
# print(bool([2, 3, 54, 'pepe', 'ricardo']))

# expresiones = [
#     False == True,
#     10 >= 2*4,
#     33/3 == 11,
#     True > False,
#     True*5 == 2.5*2
# ]

# print(expresiones)

# Operadores Logicos
# and or not

# not
# print(True)
# print(not True)
# print(not 5) # -> print(not bool(5)) 
# print(not {1,2,3,4,'pepito'}) # -> print(not bool({1,2,3,4.'pepito'})) 
# print(not {}) # -> print(not bool({})) 

# and
# True and True -> True
# False and True -> False
# True and False -> False
# False and False -> False
# print(True and True)
# print(5 == 1 and 4 < 3)
# print(5 == 1 and 'asdfq' <= 'a')

# print(True and 4/0)
# print(False and 4/0)

# print(5 and {1,2,3,4,'pepito'})

# or
# True or True -> True
# False or True -> True
# True or False -> True
# False or False -> False
# print(55 == 60 or 1.5 == 1.5)
# print(60 == 60 or 1.5 == 1.5)
# print(55 == 60 or 1.5 == 1.4)

# print(True or 4/0)
# print(False or 4/0)


# print(5 or {1,2,3,4,'pepito'})

'''
## EXPRESIONES ANIDADAS

1. Expresiones de cualquier tipo entre paréntesis.
2. Expresiones aritméticas por su propias reglas.
```
() -> ** -> / // * %  -> + -
primero -> segundo -> tercero -> cuarto
```
3. Expresiones relacionales de izquierda a derecha.
4. Operadores lógicos (not tiene prioridad ya que afecta al operando).
'''

# suma = 0
# suma += 1 # -> suma = suma + 1
# print(suma)
# suma -= 2
# print(suma)
# suma *= 3
# print(suma)
# suma /= 6
# print(suma)
# suma %= 6
# print(suma)

# texto = 'pepito'
# texto += ' corre' # -> texto = texto + ' corre'
# # texto += ' solo'
# texto *= 5

# print(texto)

## Ejercicio 3 (10min)
'''
A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable 
que almacene si se cumplen todas las siguientes condiciones, 
encadenando operadores lógicos en una sola línea:

- NOMBRE sea diferente de cuatro asteriscos “****”
- EDAD sea mayor que 5 y a su vez menor que 20
- Que la longitud de NOMBRE sea mayor o igual a 4  pero a la vez menor que 8
- EDAD multiplicada por 3 sea mayor que 35

Desde un input conseguir las variables:
nombre = INPUT!!!
edad = INPUT!!!!'''

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))

# 5 < edad and edad < 20
resultado = nombre != '****' and 5 < edad < 20 and 4 <= len(nombre) < 8 and 3*edad > 35 

print(resultado)


resultado_booleano = nombre != '****'

const pepito: true|false;

pepito: Optional[bool] = None

pepito = 'asd'