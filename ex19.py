'''
Uma loja de produtos tecnologicos te contratou para desenvolver um codigo da seguite forma:
(1)Leia um produto e de acordo com o produto verifique o preço. (Vide tabela abaixo)
(2)produtos-preço
mouse-10
teclado-20
memória-100
e (3)Leia ainda a quantidade de produtos comprados:
Calcule:
(4)total = preco * quantidade
(5)imposto = se a quantidade for maior que 10 calcule um imposto de 
5% sobre o produto senaõ calcule 10%
(6)valor final = total + imposto
'''


produto = input("Digite o produto => ").upper()

if (produto == "MOUSE"):
    preco = 10
elif (produto == "TECLADO"):
    preco = 20

elif (produto == "MEMORIA"):
    preco = 100
else:
    print("Produto não encontrado")

qtd = int(input("Digite a quantidade : ") )

total = preco * qtd

if (qtd > 10):
    imposto = total * 0.05
else:    
    imposto = total * 0.1

valor_final = total + imposto

print (f"O valor total da sua compra foi R$ {valor_final} Reais")

print (f"Voce pagou de impostos R$ {imposto} Reais")


  

