import pandas as pd

#Criando um dicionário com dados de pessoas
dict ={
    
     'Nome': ['Eduardo', 'Fernanda', 'Gabriel', 'Helena'],
     'Idade': [32, 27, 41, 36],
     'Cidade': ['Porto Alegre', 'Salvador', 'Fortaleza', 'Recife']


}

#Criando um DataFrame a partir do dicionário
df=pd.DataFrame(dict)

#Exibindo o DataFrame
print(df)