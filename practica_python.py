import pandas as pd 

df = pd.read_csv('bank_transactions_data_2_augmented_clean_2.csv')

filtro_saldo_promedio = df.groupby('CustomerOccupation')['AccountBalance'].mean()

print(filtro_saldo_promedio)