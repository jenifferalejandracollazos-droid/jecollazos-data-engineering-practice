import pandas as pd
df = pd.read_csv('transacciones.csv')

retiros = df[df['tipo'] == 'retiro']

retiros['monto_usd'] = retiros['monto'] / 4200

retiros.to_csv('retiros.csv', index=False) 

print('ELT completado')
print(retiros)
