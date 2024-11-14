# vuelo.py

class Vuelo:
    def __init__(self, origen, destino, precio, duracion):
        self.origen = origen
        self.destino = destino
        self.precio = precio
        self.duracion = duracion

    def __str__(self):
        return f"Vuelo de {self.origen} a {self.destino} - Precio: ${self.precio}, Duración: {self.duracion} horas"
