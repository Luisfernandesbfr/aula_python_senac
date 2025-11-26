import pandas as pd

dados = [
    ['Ana', 23, 'São Paulo'],
    ['Bruno', 35, 'Rio de Janeiro'],
    ['Carlos', 45,  'Belo Horizonte'],
    ['Daniela', 29, 'Curitiba']

]

colunas = ['Nome', 'Idade', 'Cidade']

df = pd.DataFrame(dados, columns=colunas)

print (df)