import pandas as pd 

clientes = {
    'cliente_id': [1, 2, 3],
    'nombre': ['Carlos', 'Lucía', 'Andrés'],
    'ciudad': ['Bogotá', 'Cali', 'Medellín']
}

transacciones = {
    'cliente_id': [1, 2, 1, 3],
    'monto': [100000, 200000, 150000, 300000]
}

def union(clientes, transacciones):
    df_clientes = pd.DataFrame(clientes)
    df_transacciones = pd.DataFrame(transacciones)
    union_tablas = pd.merge(df_clientes, df_transacciones, on='cliente_id', how='inner')
    return union_tablas

print(union(clientes, transacciones))
