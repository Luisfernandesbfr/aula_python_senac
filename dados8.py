import pandas as pd

df = pd.read_csv('ClassicDisco.csv')


#detalhes da coluna

for coluna in df.columns:
    print("Coluna",coluna)

