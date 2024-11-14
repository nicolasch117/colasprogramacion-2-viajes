# cola_vuelos.py

from vuelo import Vuelo

class Nodo:
    def __init__(self, vuelo):
        self.vuelo = vuelo
        self.siguiente = None

class ColaVuelos:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_vuelo(self, vuelo):
        nuevo_nodo = Nodo(vuelo)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def mostrar_vuelos(self, max_precio=None):
        actual = self.cabeza
        while actual:
            if max_precio is None or actual.vuelo.precio <= max_precio:
                print(actual.vuelo)
            actual = actual.siguiente
