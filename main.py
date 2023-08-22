class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarcolor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color=color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

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
