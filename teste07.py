# Exercício 7: Verificação de Letra Inicial
# Escreva um programa que peça uma palavra. Se a palavra começar com a letra 'A' (maiúscula ou minúscula), imprima "A palavra começa com 'A'."

palavra = input("Digite uma palavra ")
palavra = palavra.upper()

if palavra.lower().startswith('a'):
    print("A palavra começa com 'A'.")
else:
    print("A palavra não começa com A ")    