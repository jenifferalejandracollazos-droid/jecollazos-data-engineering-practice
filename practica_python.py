def filtrar_por_ciudad(clientes, ciudad):
    resultado = []
    for cliente in clientes:
        if cliente["ciudad"] == ciudad:
            resultado.append(cliente["nombre"])
    return resultado

clientes = [
    {"nombre": "Ana Torres", "ciudad": "Cali", "saldo": 1500000},
    {"nombre": "Carlos Ruiz", "ciudad": "Bogotá", "saldo": 3200000},
    {"nombre": "María López", "ciudad": "Medellín", "saldo": 850000},
    {"nombre": "Pedro Gómez", "ciudad": "Cali", "saldo": 4100000},
    {"nombre": "Lucía Herrera", "ciudad": "Bogotá", "saldo": 620000}
]

print(filtrar_por_ciudad(clientes, "Cali"))
print(filtrar_por_ciudad(clientes, "Bogotá"))