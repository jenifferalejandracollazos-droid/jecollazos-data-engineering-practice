import pandas as pd

clientes = {
    "nombre": ["Ana Torres", "Carlos Ruiz", "María López", "Pedro Gómez", "Lucía Herrera"],
    "ciudad": ["Cali", "Bogotá", "Medellín", "Cali", "Bogotá"],
    "saldo": [1500000, 3200000, 850000, 15000000, 620000]
}

df = pd.DataFrame(clientes)

media = df["saldo"].mean()
desviacion = df["saldo"].std()

outliers = df[(df["saldo"] > media + 2*desviacion) | (df["saldo"] < media - 2*desviacion)]

print("Media:", media)
print("Desviación:", desviacion)
print(outliers)
