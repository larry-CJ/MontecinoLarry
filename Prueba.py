import random
import csv
from statistics import mean, geometric_mean
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
def calcular_estadisticas(saldos):
    saldos_lista = list(saldos.values())
    saldo_alto = max(saldos_lista)
    saldo_bajo = min(saldos_lista)
    saldo_promedio = mean(saldos_lista)
    media_geo = geometric_mean(saldos_lista)
    return saldo_alto, saldo_bajo, saldo_promedio, media_geo
    
def generar_reporte(saldos, impuestos):
    with open('reporte_saldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Cliente', 'Saldo Bruto ($)', 'impuestos ($)', 'Saldo Neto ($)'])
        for cliente, saldo in saldos.items():
            impuesto = impuestos.get(cliente, 0)
            saldo_neto = round(saldo - impuesto, 2)
            writer.writerow([cliente, saldo, impuesto, saldo_neto])
            
def mostrar_menu():
    print("Menú:")
    print("1. Asignar saldos")
    print("2. Clasificar saldos")
    print("3. Ver estadísticas")
    print("4. Generar reporte")
    print("5. Salir")
    
def main():
    saldos = {}
    impuestos = {}
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
                rango_bajo, rango_prodemio, rango_alto = clasificar_saldos(saldos)
                print("\nRangos de saldos:")
                print("Rango bajo (<3000):", rango_bajo)
                print("Rango medio (3000-7000):", rango_prodemio)
                print("Rango alto (>7000):", rango_alto)
                
        elif opcion == '3':
            if not saldos:
                print("Primero debe asignar los saldos.")
            else:
                saldo_alto, saldo_bajo, saldo_promedio, media_geo = calcular_estadisticas(saldos)
                print("Estadísticas:")
                print(f"Saldo más alto: ${saldo_alto:.2f}")
                print(f"Saldo más bajo: ${saldo_bajo:.2f}")
                print(f"Saldo promedio: ${saldo_promedio:.2f}")
                print(f"Media geométrica: ${media_geo:.2f}")
           
        elif opcion == '4':
            if not saldos:
                print("Primero debe asignar los saldos.")
            else:    
                impuestos = {cliente[0]: round(random.uniform(50, 500), 2) for cliente in clientes[1:]} 
                generar_reporte(saldos, impuestos)
                print("Reporte de saldos generado en 'reporte_saldos.csv'.")

        elif opcion == '5':
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor seleccione una opción del menú.")

if __name__ == "__main__":
    main()
    
