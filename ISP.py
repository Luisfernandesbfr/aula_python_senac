<<<<<<< HEAD
#importando a biblioteca pandas
import pandas as pd

#Ler arquivo CSV da ISP RJ
df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep = ';', encoding='latin1')

#exibir 5 primeiras linhas do DataFrame
#print(df.head())

#descrever o DataFrame
#print(df.describe())

#exibir 5 últimas linhas do DataFrame
#print(df.tail())

#Agrupar os dados por CISP e somar o número de roubos de celulares
df_roubo_celular_dp = df.groupby('cisp')['roubo_celular'].sum().reset_index()
df_roubo_celular_dp = df_roubo_celular_dp.sort_values(by='roubo_celular', ascending=False)

#exibir o DataFrame resultante
print(df_roubo_celular_dp)
=======
#importando a biblioteca pandas
import pandas as pd

#Ler arquivo CSV da ISP RJ
df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep = ';', encoding='latin1')

#exibir 5 primeiras linhas do DataFrame
#print(df.head())

#descrever o DataFrame
#print(df.describe())

#exibir 5 últimas linhas do DataFrame
#print(df.tail())

#Agrupar os dados por CISP e somar o número de roubos de celulares
df_roubo_celular_dp = df.groupby('cisp')['roubo_celular'].sum().reset_index()
df_roubo_celular_dp = df_roubo_celular_dp.sort_values(by='roubo_celular', ascending=False)

#exibir o DataFrame resultante
print(df_roubo_celular_dp)
>>>>>>> 3786d477a219c6a94791467270ccaab7c665468a
