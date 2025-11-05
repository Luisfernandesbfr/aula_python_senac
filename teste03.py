# Exercício 3: Verificação de Nota Aprovativa
# Escreva um programa que peça uma nota (de 0 a 10). Se a nota for maior ou igual a 7, imprima "Parabéns, você foi aprovado!"

nota = float(input("Digite uma nota de 0 a 10: "))

if (nota >= 7):
    print("Parabéns, voce foi aprovado!")
else :
    print("Voce está de recuperação")    