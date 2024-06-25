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
    ['10.María'],
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
