# main.py

from cola_vuelos import ColaVuelos
from app import agregar_vuelo, mostrar_vuelos_economicos

def main():
    cola_vuelos = ColaVuelos()
    while True:
        print("\n--- Aplicación de Viajes ---")
        print("1. Agregar vuelo")
        print("2. Mostrar vuelos económicos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_vuelo(cola_vuelos)
        elif opcion == '2':
            mostrar_vuelos_economicos(cola_vuelos)
        elif opcion == '3':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
