
# ================================================================================
# ================================================================================

    
# class Motor:
#     def __init__(self, numero_serie, cant_cilindros = 6):
#         self.numero_serie = numero_serie
#         self.cant_cilindros = cant_cilindros
        
# class Auto:
    
#     cant_ruedas = 4
    
#     def __init__(self, marca, modelo, num_chasis, color='Blanco', **datos_de_motor):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(**datos_de_motor) # -> Motor(n_serie=123456, cant_cilindros=12)
#         self.__num_chasis = num_chasis
#         print(f'Se creo el auto {self}')

#     def __str__(self):
#         return f'Auto {self.marca} {self.modelo} de color {self.color}'

#     def __tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!', self)
        
#     def avanzar(self, metros_a_avanzar):
#         self.__tocar_bocina()
#         print('El auto', self, 'avanzo', metros_a_avanzar, 'metros')

#     def mostrar_num_chasis(self): # -> getter
#         if self.color != 'Blanco':
#             print(f'El numero de chasis para {self} es {self.__num_chasis}')
#         else:
#             print('No te lo puedo mostrar porque soy un auto blanco.')
            
#     def actualizar_num_chasis(self, nuevo_num_chasis): # -> setter
#         if self.color != 'Blanco':
#             self.__num_chasis = nuevo_num_chasis
#         else:
#             print('No puedo modificar mi num chasis porque soy un auto blanco.')

# auto1 = Auto('Ford', 'K', 123456, 'Rojo', numero_serie=123456, cant_cilindros=12)
# # print(auto1.__num_chasis)
# # print(auto1._Auto__num_chasis)
# auto1.mostrar_num_chasis()
# auto1.actualizar_num_chasis(555)
# auto1.mostrar_num_chasis()


# # ================================================================================
# # ================================================================================

# class Vehiculo:
    
#     def __init__(self, marca, color):
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
        
#     def __str__(self):
#         return f'{type(self).__name__} {self.marca} de color {self.color}'

#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!')


# class Auto(Vehiculo):
#     ...
#     # def __str__(self):
#     #     return f'Este es el str del auto'
    
# class Moto(Vehiculo):
#     ...
#     # def __str__(self):
#     #     return f'Este es el str de la moto'
    
# class Lancha(Vehiculo):
#     ...
    

# vehiculo = Vehiculo('Ford', 'verde')
# print(vehiculo)
# vehiculo.tocar_bocina()

# auto = Auto('Fiat', 'blanco')
# print(auto)
# auto.tocar_bocina()

# moto = Moto('BMW', 'negra')
# print(moto)
# moto.tocar_bocina()

# lancha = Lancha('Lamborghini', 'blanca')
# print(lancha)
# lancha.tocar_bocina()

# autito = auto
# print(autito)

# # ================================================================================
# # ================================================================================

# class Vehiculo:
    
#     def __init__(self, marca, color):
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
        
#     def __str__(self):
#         return f'{type(self).__name__} {self.marca} de color {self.color}'

#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!')
        
#     def __metodo_solo_vehiculo(self):
#         print('Metodo solo de Vehiculo!!!')


# class Auto(Vehiculo):
    
#     # v1
#     # def __init__(self, marca, color, cant_ruedas):
#     #     self.marca = marca
#     #     self.color = color
#     #     self.cant_ruedas = cant_ruedas
#     #     print(f'Se creo {self}')
        
#     # v2
#     def __init__(self, marca, color, cant_ruedas):
#         self.cant_ruedas = cant_ruedas
#         super().__init__(marca, color)
        
#     # v3
#     # def __init__(self, cant_ruedas, **kwargs):
#     #     self.cant_ruedas = cant_ruedas
#     #     super().__init__(**kwargs)
    
#     def tocar_bocina(self):
#         super().tocar_bocina()
#         print('Soy el auto tocando bocina')
#         super().tocar_bocina()
        
#     def metodo_solo_auto(self):
#         super().__metodo_solo_vehiculo()
#         print('Metodo solo de Auto!!!')



# vehiculo = Vehiculo('Ford', 'verde')
# print(vehiculo)
# vehiculo.tocar_bocina()

# # v2
# auto = Auto('Fiat', 'blanco', 4)

# # v3
# # auto = Auto(marca='Fiat', color='blanco', cant_ruedas=4)
# # auto = Auto(4, marca='Fiat', color='blanco')
# print(auto.cant_ruedas)
# auto.tocar_bocina()
# # auto.__metodo_solo_vehiculo()
# auto.metodo_solo_auto()

# # ================================================================================
# # ================================================================================

# class Vehiculo:
    
#     def __init__(self, marca, color):
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
        
#     def __str__(self):
#         return f'{type(self).__name__} {self.marca} de color {self.color}'

#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!')


# class VehiculosConRuedas(Vehiculo):
    
#     def __init__(self, marca, color, cant_ruedas):
#         self.cant_ruedas = cant_ruedas
#         super().__init__(marca, color)
        
    
# class Auto(VehiculosConRuedas):
#     ...
    
# class Moto(VehiculosConRuedas):
#     ...
    
# class Lancha(Vehiculo):
#     ...
    


# auto = Auto('Fiat', 'blanco', 4)
# moto = Moto('BMW', 'negra', 2)
# lancha = Lancha('Lamborghini', 'blanca')

# print(auto.cant_ruedas)
# print(moto.cant_ruedas)

# auto.tocar_bocina()
# lancha.tocar_bocina()


# # ================================================================================
# # ================================================================================

# class Vehiculo:
    
#     def __init__(self, marca, color):
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
        
#     def __str__(self):
#         return f'{type(self).__name__} {self.marca} de color {self.color}'

#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!')


# class VehiculosConRuedas(Vehiculo):
    
#     def __init__(self, marca, color, cant_ruedas):
#         self.cant_ruedas = cant_ruedas
#         super().__init__(marca, color)
        
        
# class Acuatico():
    
#     def avanzar(self, millas_a_avanzar):
#         print('El', type(self).__name__, 'avanzo', millas_a_avanzar, 'millas')

# class Terrestre():
    
#     def avanzar(self, metros_a_avanzar):
#         print('El', type(self).__name__, 'avanzo', metros_a_avanzar, 'metros')


# class Auto(VehiculosConRuedas, Terrestre):
#     ...
    
# class Lancha(Vehiculo, Acuatico):
#     ...


# auto = Auto('Fiat', 'blanco', 4)
# lancha = Lancha('Lamborghini', 'blanca')

# auto.avanzar(15)
# lancha.avanzar(20)


# ================================================================================
# ================================================================================

# class Vehiculo:
    
#     def __init__(self, marca, color):
#         self.marca = marca
#         self.color = color
#         print(f'Se creo {self}')
        
#     def __str__(self):
#         return f'{type(self).__name__} {self.marca} de color {self.color}'

#     def tocar_bocina(self):
#         print('PIPIIIIIIIIIIIIIIIIIIIIIIII!!!')

# class Acuatico():
    
#     def avanzar(self, millas_a_avanzar):
#         print('El', type(self).__name__, 'avanzo', millas_a_avanzar, 'millas')

# class Terrestre():
    
#     def __init__(self, cant_ruedas):
#         self.cant_ruedas = cant_ruedas
    
#     def avanzar(self, metros_a_avanzar):
#         print('El', type(self).__name__, 'avanzo', metros_a_avanzar, 'metros')


# class Auto(Vehiculo, Terrestre):
#     def __init__(self, marca, color, cant_ruedas):
#         super().__init__(marca, color)
        
#     def tocar_bocina(self):
#         print('Toque bocina en mi auto')
        
    
# class Lancha(Vehiculo, Acuatico):
#     ...
    
#     def tocar_bocina(self):
#         print(f'Toque bocinaaaaa en mi lancha {self.marca}')


# auto = Auto('Fiat', 'blanco', 4)
# lancha = Lancha('Lamborghini', 'blanca')

# auto.avanzar(15)
# lancha.avanzar(20)

# print(Auto.__mro__)
# print(Vehiculo.__mro__)

# lista = [auto, lancha]


# for objeto in lista:
#     objeto.tocar_bocina()
