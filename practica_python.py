import pandas as pd

clientes = {
    "nombre": ["Ana Torres", "Carlos Ruiz", "María López", "Pedro Gómez", "Lucía Herrera"],
    "ciudad": ["Cali", "Bogotá", "Medellín", "Cali", "Bogotá"],
    "saldo": [1500000, 3200000, 850000, 4100000, 620000]
}

df = pd.DataFrame(clientes)

media = df['saldo'].mean()
desviacion = df['saldo'].std()

print(media)
print(desviacion)