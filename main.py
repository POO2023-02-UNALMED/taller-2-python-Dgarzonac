class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = color

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
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.registro = registro
        self.motor = motor
        Auto.cantidadCreados += 1

    def verificarIntegridad(self):
        registro_auto = self.registro
        verificador = True
    
        if self.motor.registro != registro_auto:
            verificador = False
    
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != registro_auto:
                verificador = False
                break
    
        if verificador:
            return 'Auto original'
        else:
            return 'Las piezas no son originales'
    
            
    def cantidadAsientos(self):
        num_asientos =0
        for i in self.asientos:
            if i is not None:
                num_asientos+=1
        return num_asientos
