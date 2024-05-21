
# print(r"c\no_ta_loco\tortita_de_manteca")

# print(r"https://docs.google.com/presentation/d/1lDuvXwi0Pea5cfc0qNaEvw7O3VCx1lohj5BCR0v3_3o/edit#slide=id.p19")
# direccion = input("ingresa la url: ")
# print(direccion)

# # import os
# import sys

# print(sys.argv)

# suma = 0
# for valor in sys.argv[1:]:
#     suma += int(valor)

# # valor1 = int(input("ingresa un valor"))
# # valor2 = int(input("ingresa otro valor"))

# print(f"La suma de {sys.argv[1:]} es {suma}")

#=================================================
#=================================================

# import sys

# print(sys.argv)

# valores = sys.argv[1:]

# if len(valores) == 2:
#     print(f"La suma de {valores[0]} y {valores[1]}"
#            f" es {int(valores[0])+ int(valores[1])}")
# else:
#     print('No me podes pasar ni mas ni menos de 2 valores numericos')

#=================================================
#=================================================

# v1

# import operacion

# print(operacion.sumar(2,4))
# print(operacion.restar(2,4))

# cuadrado = operacion.Cuadrado(5)
# print(cuadrado.perimetro())

# print(operacion.var_de_operacion)

#=================================================
#=================================================

# v2
# from operacion import sumar, restar, Cuadrado, var_de_operacion

# print(sumar(2,4))
# print(restar(2,4))

# cuadrado = Cuadrado(5)
# print(cuadrado.perimetro())

# print(var_de_operacion)

#=================================================
#=================================================

# v3
# from operacion import *
# # from operacion import sumar, restar, Cuadrado, var_de_operacion


# print(sumar(2,4))
# print(restar(2,4))

# cuadrado = Cuadrado(5)
# print(cuadrado.perimetro())

# print(var_de_operacion)

#=================================================
#=================================================

# v4
# from operacion import sumar as sumar_de_operaciones, restar, Cuadrado, var_de_operacion


# def sumar():
#     print('Sumo lo que quiero')


# print(sumar_de_operaciones(2,4))
# print(restar(2,4))



# cuadrado = Cuadrado(5)
# print(cuadrado.perimetro())

# print(var_de_operacion)

#=================================================
#=================================================

# from matematica.operacion import sumar as sumar_de_operaciones, restar, Cuadrado, var_de_operacion


# def sumar():
#     print('Sumo lo que quiero')


# print(sumar_de_operaciones(2,4))
# print(restar(2,4))



# cuadrado = Cuadrado(5)
# print(cuadrado.perimetro())

# print(var_de_operacion)


#=================================================
#=================================================


# from matematica.operacion import sumar

# print(sumar(2,2))


#=================================================
#=================================================

