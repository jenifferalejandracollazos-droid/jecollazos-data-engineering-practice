import pandas as pd

df = pd.read_csv('transacciones.csv')

retiros = df[df['tipo'] == 'retiro']
retiros['monto_usd'] = retiros['monto'] / 4200
retiros['es_alto'] = retiros['monto'] > 600000

retiros.to_csv('retiros_analizados.csv', index=False)

print('ETL completado')
print(retiros)