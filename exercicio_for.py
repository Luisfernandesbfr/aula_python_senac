<<<<<<< HEAD
'''Você foi contratado para desenvolver um sistema simples de cadastro de 
produtos para uma loja. O sistema deve:
 Solicitar ao usuário quantos produtos desejar cadastrar.
 Para cada produto, solicitar:
 O nome do produto.
 O valor do produto.
 Armazenar os nomes em uma lista e os valores em outra lista.
 Ao final, exibir um relatório com todos os produtos e seus 
respectivos valore'''


n_produtos = []
v_produtos = []

qtd_produtos = int(input("Quantos produtos você deseja cadastrar? "))

for i in range(qtd_produtos):
    nome = input(f"Digite o nome do produto {i + 1}: ")
    valor = float(input(f"Digite o valor do produto {i + 1}: "))
    
    n_produtos.append(nome)
    v_produtos.append(valor) 

print("\n--- Relatório de Produtos Cadastrados ---")   
for nome, valor in zip(n_produtos, v_produtos):
    print(f"Produto: {nome} - Valor: R$ {valor:.2f}")





=======
'''Você foi contratado para desenvolver um sistema simples de cadastro de 
produtos para uma loja. O sistema deve:
 Solicitar ao usuário quantos produtos desejar cadastrar.
 Para cada produto, solicitar:
 O nome do produto.
 O valor do produto.
 Armazenar os nomes em uma lista e os valores em outra lista.
 Ao final, exibir um relatório com todos os produtos e seus 
respectivos valore'''


n_produtos = []
v_produtos = []

qtd_produtos = int(input("Quantos produtos você deseja cadastrar? "))

for i in range(qtd_produtos):
    nome = input(f"Digite o nome do produto {i + 1}: ")
    valor = float(input(f"Digite o valor do produto {i + 1}: "))
    
    n_produtos.append(nome)
    v_produtos.append(valor) 

print("\n--- Relatório de Produtos Cadastrados ---")   
for nome, valor in zip(n_produtos, v_produtos):
    print(f"Produto: {nome} - Valor: R$ {valor:.2f}")





>>>>>>> 3786d477a219c6a94791467270ccaab7c665468a
