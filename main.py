from motor import Motor
from asiento import Asiento

class Auto:
    cantidadCreados=0
    
    def __init__(self, modelo, precio, asientos, marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.registro=registro
        self.motor=motor
        Auto.cantidadCreados+=1

    def verificarintegridad(self, auto):
        registro1=auto.registro
        verificador= False
        if auto.motor.registro == registro1:
            verificador=True
            for i in auto.asientos:
                if i.registro != registro1:
                    verificador = False
                    break
        
        if verificador:
            print('Auto original')
        
        else:
            print('Las piezas no sonoriginales')

motor1 = Motor(4, "gasolina", "ABC123")
asientos = [Asiento("rojo", 100, "XYZ001"), Asiento("verde", 120, "XYZ002")]

# Crear instancia de Auto
auto1 = Auto("Sedán", 20000, asientos, "Toyota", motor1, "AUTO001")

# Verificar integridad
auto2 = Auto("SUV", 35000, asientos, "Honda", motor1, "AUTO002")
auto1.verificarIntegridad(auto2)