import pandas as pd

df = pd.read_csv('transacciones.csv')
df['monto_cop'] = df['monto'] * 1.05
df.to_csv('transacciones_ajustadas.csv', index=False)

print('ETL terminado')
print(df)

