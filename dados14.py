<<<<<<< HEAD
import pandas as pd

dados = [
    ['Ana', 23, 'São Paulo'],
    ['Bruno', 35, 'Rio de Janeiro'],
    ['Carlos', 45,  'Belo Horizonte'],
    ['Daniela', 29, 'Curitiba']

]

colunas = ['Nome', 'Idade', 'Cidade']

df = pd.DataFrame(dados, columns=colunas)

=======
import pandas as pd

dados = [
    ['Ana', 23, 'São Paulo'],
    ['Bruno', 35, 'Rio de Janeiro'],
    ['Carlos', 45,  'Belo Horizonte'],
    ['Daniela', 29, 'Curitiba']

]

colunas = ['Nome', 'Idade', 'Cidade']

df = pd.DataFrame(dados, columns=colunas)

>>>>>>> 3786d477a219c6a94791467270ccaab7c665468a
print (df)