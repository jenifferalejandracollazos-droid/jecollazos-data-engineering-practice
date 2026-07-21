import pandas as pd 

df = pd.read_csv('transacciones.csv')
agrupar = df.groupby('tipo')['monto'].agg(['sum', 'mean', 'count']).reset_index()
agrupar.to_csv('estadisticas_por_grupo.csv', index=False)

print(agrupar)