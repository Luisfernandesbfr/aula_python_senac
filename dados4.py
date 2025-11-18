import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

print(df.columns)

filtro = df[['Artist','Track','Year','Album']]

print(filtro)

