import pandas as pd 

df = pd.read_csv('transacciones.csv')
monto_total = df.groupby('tipo')['monto'].sum().reset_index()
monto_total.to_csv('resumen_tipos.csv', index=False)


print(monto_total)
