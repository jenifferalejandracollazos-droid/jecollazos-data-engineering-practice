import pandas as pd 

clientes = [
    {"id": 1, "nombre": "Ana", "edad": 28, "monto_gastado": 150.50, "activo": True},
    {"id": 2, "nombre": "Carlos", "edad": 35, "monto_gastado": 420.00, "activo": True},
    {"id": 3, "nombre": "María", "edad": 42, "monto_gastado": 85.20, "activo": False},
    {"id": 4, "nombre": "Luis", "edad": 23, "monto_gastado": 210.10, "activo": True},
    {"id": 5, "nombre": "Elena", "edad": 31, "monto_gastado": 340.00, "activo": False}
]

def promedio_clientes(clientes):
    df = pd.DataFrame(clientes)
    promedio = df['monto_gastado'].mean()
    return round(promedio, 2)

print(promedio_clientes(clientes))

