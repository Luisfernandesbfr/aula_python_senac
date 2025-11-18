import pandas as pd

df = pd.read_csv('ClassicDisco.csv')


#exibe numeros de linhas e colunas
print(df.shape)


#exibe nome das colunas
print(df.columns)