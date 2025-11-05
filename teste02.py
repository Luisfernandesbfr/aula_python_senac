# Exercício 2: Verificação de Idade para Votar
# Escreva um programa que pergunte a idade do usuário. Se a idade for 16 anos ou mais, imprima "Você já pode votar."

idade = int(input("Digite sua idade: "))

if(idade >= 16):
    print("Voce ja pode votar ")
else :
    print("Voce ainda não pode votar ")    