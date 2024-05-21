# =========================================================
# =========================================================
# v1
# =========================================================
# =========================================================
class Cajero:
    
    usuarios = {}
    
    def __init__(self):
        self.__agregar_usuarios()
        
    def __agregar_usuarios(self):
        agregar_usuario = True # bandera/flag
        while agregar_usuario:
            if input('Quiere agregar un usuario: (ingrese si en caso correcto)') != 'si':
                break
            ingreso_nuevo_usuario = input('Ingrese el usuario: ')
            ingreso_contrasenia_del_nuevo_usuario = input('Ingrese la contrasenia: ')
            self.usuarios[ingreso_nuevo_usuario] = ingreso_contrasenia_del_nuevo_usuario
            
    def __autenticar(self, usuario, contrasenia):
        return self.usuarios.get(usuario) == contrasenia
        
    
    def __login(self):
        ingreso_de_usuario = input('Ingrese su usuario: ')
        ingreso_de_contrasenia = input('Ingrese su contrasenia: ')
        if self.__autenticar(ingreso_de_usuario, ingreso_de_contrasenia):
            print('Inicio sesion con exito!')
            return True
        elif ingreso_de_usuario == 'sal' and ingreso_de_contrasenia == 'ir':
            return
        else:
            print('Error! Vuelva a intentarlo!')
            return False
    
    def iniciar_cajero(self):
        repetir_autenticacion = True # bandera/flag
        while repetir_autenticacion:
            conectado = self.__login()
            if conectado == False:
                continue
            elif conectado == None:
                break
            self.__menu()
                
    
    def __menu(self):
        repetir_menu = True # bandera/flag
        while repetir_menu:
            print('''
        ==============
            Menu
        ==============
        1. Retirar efectivo.
        2. Cambiar contraseña.
        3. Salir
        ''')
            opcion_elegida = input('Ingrese la operacion a realizar: ')
            if opcion_elegida == '1':
                self.__retiro_efectivo()
            elif opcion_elegida == '2':
                self.__cambiar_contrasenia()
            elif opcion_elegida == '3':
                repetir_menu = False
                print('Hasta luego!')
            else:
                print('Vuelva a intentar con una opcion valida.')
        
    def __retiro_efectivo(self):
        print('Retiro efectivo.')
    
    def __cambiar_contrasenia(self):
        print('Cambio la contraseña.')
        
cajero1 = Cajero()
cajero1.iniciar_cajero()
print('Estos son los usuario de cajero1', cajero1.usuarios)


cajero2 = Cajero()
print('Estos son los usuario de cajero2', cajero2.usuarios)


# =========================================================
# =========================================================
# v2
# =========================================================
# =========================================================

class Tarjeta:
    def __init__(self, nro_tarjeta=None):
        self.nro_tarjeta = nro_tarjeta

class Persona:
    def __init__(self, nombre, apellido, tarjeta):
        self.nombre = nombre
        self.apellido = apellido
        self.__tarjeta = tarjeta

    def get_tarjeta(self, entidad_solicitante):
        if type(entidad_solicitante) == Cajero:
            return self.__tarjeta # Trabajando con solo el numero de tarjeta en string
            # return self.__tarjeta.nro_tarjeta # Trabajando con la clase Tarjeta
        

class Cajero:
    
    def __init__(self):
        self.datos_cuentas = [
            {
                'nro_tarjeta': '123456789',
                'contrasenia': 'pinocho',
                'fondo': 1000,
            },
            {
                'nro_tarjeta': '987654321',
                'contrasenia': 'miami',
                'fondo': 99999999999,
            }
        ]
    
    def autenticar(self, persona_a_autenticar):
        nro_tarjeta = persona_a_autenticar.get_tarjeta(self)
        contrasenia = input('Ingresa tu contrasenia: ')
        for cuenta in self.datos_cuentas:
            if (
                cuenta.get('nro_tarjeta') == nro_tarjeta and
                cuenta.get('contrasenia') == contrasenia
            ):
                self.__menu()
                return
        print('El numero de tarjeta o contrasenia no existen.')
    
    def __menu(self):
        repetir_menu = True # bandera/flag
        while repetir_menu:
            print('''
        ==============
            Menu
        ==============
        1. Retirar efectivo.
        2. Cambiar contraseña.
        3. Salir
            ''')
            opcion_elegida = input('Ingrese la operacion a realizar: ')
            if opcion_elegida == '1':
                self.__retirar_efectivo()
            elif opcion_elegida == '2':
                self.__cambiar_contrasenia()
            elif opcion_elegida == '3':
                print('Hasta luego!')
                repetir_menu = False
            else:
                print('Vuelva a intentar con una opcion valida.')
        
    def __cambiar_contrasenia(self):
        print('Cambio la contraseña.')
        
    def __retirar_efectivo(self):
        print('Retiro efectivo.')
    

           
# Trabajando con la clase Tarjeta
# tarjeta1 = Tarjeta('123456789')
# tarjeta2 = Tarjeta('987654321')

# persona1 = Persona('Pepe', 'Grillo', tarjeta1)
# persona2 = Persona('Ricardo', 'Fort', tarjeta2)


# Trabajando con solo el numero de tarjeta en string
persona1 = Persona('Pepe', 'Grillo', '123456789')
persona2 = Persona('Ricardo', 'Fort', '987654321')


# Esto es igual para cualquiera de las 2 formas usadas antes
# print(persona1.__tarjeta)
# print(persona1.get_tarjeta(persona2))
    
cajero = Cajero()
# cajero.autenticar(persona1)
cajero.autenticar(persona2)
# cajero.__menu()

# =========================================================
# =========================================================
# v3
# =========================================================
# =========================================================

import json

class Cajero:
    
    archivo_datos = 'datos.json'
    
    def prender(self):
        bandera1 = True
        while bandera1 != False:
            if input('Desea agregar nuevos usuarios? (si o no)') == 'si':
                self.__agregar_usuarios()
            else:
                bandera1 = False
        bandera2 = True
        while bandera2 != False:
            bandera2 = self.__loguearse()
    
    def __loguearse(self):
        nro_tarjeta = input('Ingresar numero de tarjeta: ')
        contrasenia = input('Ingresar numero de contrasenia: ')
        if nro_tarjeta + contrasenia == 'salir':
            return False
        if self.__autenticar_usuario(nro_tarjeta, contrasenia):
            self.__menu()
        else:
            print('Los datos ingresados no son correctos. Vuelva a intentarlo.')
    
    def __autenticar_usuario(self, nro_tarjeta, contrasenia):
        with open(Cajero.archivo_datos, 'r') as f:
            datos = json.load(f)
        for nro_tarjeta_guardada, contrasenia_guardada in datos.items():
            if nro_tarjeta == nro_tarjeta_guardada and contrasenia == contrasenia_guardada:
                return True
    
    def __agregar_usuarios(self):
        with open(Cajero.archivo_datos, 'r') as f:
            datos = json.load(f)
        
        nro_tarjeta = input('Ingrese numero de tarjeta del nuevo usuario: ')
        contrasenia = input('Ingrese contrasenia del nuevo usuario: ')
        datos[nro_tarjeta] = contrasenia
        
        with open(Cajero.archivo_datos, 'w') as f:
            json.dump(datos, f, indent=4)
            
    
    def __menu(self):
        repetir_menu = True # bandera/flag
        while repetir_menu:
            print('''
        ==============
            Menu
        ==============
        1. Retirar efectivo.
        2. Cambiar contraseña.
        3. Salir
        ''')
            opcion_elegida = input('Ingrese la operacion a realizar: ')
            if opcion_elegida == '1':
                self.__retirar_efectivo()
            elif opcion_elegida == '2':
                self.__cambiar_contrasenia()
            elif opcion_elegida == '3':
                print('Hasta luego!')
                repetir_menu = False
            else:
                print('Vuelva a intentar con una opcion valida.')
                
    def __cambiar_contrasenia(self):
        print('Cambio la contraseña.')
        
    def __retirar_efectivo(self):
        print('Retiro efectivo.')

with open(Cajero.archivo_datos, 'a') as f:
    print('Se inicializo el archivo de datos!')
cajero = Cajero()
cajero.prender()