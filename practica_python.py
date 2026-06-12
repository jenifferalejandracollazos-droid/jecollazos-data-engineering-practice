import pandas as pd
df = pd.read_csv('transacciones.csv')

retiros = df[df['tipo'] == 'retiro']

retiros.to_csv('retiros.csv, index=False')

print('ETL completado')
print(retiros)