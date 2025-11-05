# Exercício 6: Verificação de Desconto
# Escreva um programa que pergunte o valor de uma compra. Se o valor for superior a R$ 100,00, imprima "Você tem direito a um desconto!"

valor = float(input("Qual o valor da compra (R$): "))

if valor > 100:
    print("Você tem direito a desconto ")
else :
    print(" Você não tem direito a desconto")    