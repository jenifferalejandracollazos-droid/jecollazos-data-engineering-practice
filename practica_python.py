import pandas as pd

df = pd.read_csv('transacciones.csv')

resumen_por_tipo = df.groupby('tipo')['monto'].sum().reset_index()

resumen_por_tipo.to_csv('resumen_por_tipo.csv', index=False)

print('ETL completado')
print(resumen_por_tipo)