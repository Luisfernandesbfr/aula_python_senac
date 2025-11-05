# Exercício 5: Verificação de Número Par
# Escreva um programa que peça um número inteiro. Se o número for par (ou seja, o resto da divisão por 2 é 0), imprima "O número é par

numero = int(input("Digite um numero: "))

if numero % 2 == 0 :
    print("O numero é par")
else:
    print("O numero é impar")    