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
