import random
import csv

# Lista de clientes
clientes = [
    ['Nombre'],
    ['1.Pedro'],
    ['2.Ana'],
    ['3.Luis'],
    ['4.Juan'],
    ['5.Larry'],
    ['6.Miguel'],
    ['7.Diego'],
    ['8.Felipe'],
    ['9.Andres'],
    ['10.Maria'],
]
def asignar_saldos(clientes):
    saldos = {cliente[0]: round(random.uniform(1000, 10000), 2) for cliente in clientes[1:]} 
    return saldos
    
def clasificar_saldos(saldos):
    rango_bajo, rango_prodemio, rango_alto = [], [], []
    for cliente, saldo in saldos.items():
        if saldo < 3000:
            rango_bajo.append((cliente, saldo))
        elif 3000 <= saldo < 7000:
            rango_prodemio.append((cliente, saldo))
        else:
            rango_alto.append((cliente, saldo))
    return rango_bajo, rango_prodemio, rango_alto
    
def mostrar_menu():
    print("Menú:")
    print("1. Asignar saldos")
    print("2. Clasificar saldos")
    print("3. Ver estadísticas")
    print("4. Generar reporte")
    print("5. Salir")
    
def main():
    saldos = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            saldos = asignar_saldos(clientes)
            print("Saldos asignados (en dólares):")
            for cliente, saldo in saldos.items():
                print(f"{cliente}: ${saldo:.2f}")

        elif opcion == '2':
            if not saldos:
                print("Primero debe asignar los saldos.")
            else:
      
        elif opcion == '3':
            if not saldos:
                print("Primero debe asignar los saldos.")
            else:
           
        elif opcion == '4':
            if not saldos:
                print("Primero debe asignar los saldos.")
            else:

        elif opcion == '5':
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor seleccione una opción del menú.")

if __name__ == "__main__":
    main()
    
