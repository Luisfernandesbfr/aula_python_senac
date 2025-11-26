''' Você deve criar um programa que simule o 
cadastro e a consulta de informações de um 
produto em uma loja'''

#Criando um dicionário com informações do produto
produto =  {
    'Nome': 'Mousse',
    'Preço': 49.90,
    'Estoque': 25,    
}

#Exibindo as informações do produto
for chave, valor in produto.items():
 print(f"{chave}: {valor}")

#Consultando informações específicas do produto
chave_consulta = input("Digite o nome de uma chave para consultar (Ex: Nome, Preço, Estoque): ").strip()

#Formatando a chave para corresponder ao formato do dicionário
chave_formatada = chave_consulta.capitalize()

#Obtendo o valor correspondente à chave informada
valor_encontrado = produto.get(chave_formatada, "Essa informação não está disponível.")

#Exibindo o resultado da consulta
print(f"{chave_formatada}: {valor_encontrado}")

#Adicionando uma nova informação ao dicionário
produto['Categoria'] = 'informatica'


produto['Preço'] =  59.90

del produto['Estoque']

print("\nInformações atualizadas do produto:")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")

    