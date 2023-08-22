class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarcolor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color=color
        