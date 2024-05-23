class ClaseDePrueba:
    atributo1 = 'Dato'
    
    def __init__(self, asd):
        # self.atributo2 = 'Dato2'
        self.atributo2 = asd
    
    def __str__(self):
        return 'Este es el mensaje del str'
    
    def saltar(self):    
        print('Saltando como loco!')
        
    def saltar2(self):
        print('Saltando como loco2!')
        
clase1 = ClaseDePrueba('prueba')
clase1.saltar()
dato = clase1
print(dato)

dato2 = str(clase1)
print(dato2)



# from productos.productos import listaprocdutos as nuevo_nombre

# listaprocdutosa= asd

# nuevo_nombre



# from paquete_entrega.cliente import Cliente

# lo que esta en el condicional
