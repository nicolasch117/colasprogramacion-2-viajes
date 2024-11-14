# app.py

from vuelo import Vuelo
from cola_vuelos import ColaVuelos

def agregar_vuelo(cola_vuelos):
    origen = input("Ingrese el origen del vuelo: ")
    destino = input("Ingrese el destino del vuelo: ")
    precio = float(input("Ingrese el precio del vuelo: "))
    duracion = float(input("Ingrese la duración del vuelo (horas): "))

    vuelo = Vuelo(origen, destino, precio, duracion)
    cola_vuelos.agregar_vuelo(vuelo)
    print("Vuelo agregado con éxito.")

def mostrar_vuelos_economicos(cola_vuelos):
    max_precio = float(input("Ingrese el precio máximo para filtrar vuelos económicos: "))
    print("\nVuelos económicos:")
    cola_vuelos.mostrar_vuelos(max_precio=max_precio)
