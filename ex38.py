""" Defina um número secreto (por exemplo, 42). Crie um programa que peça ao usuário para adivinhar esse número.
 Use um loop while para repetir a pergunta até que o palpite esteja correto.
 Use instruções if, elif e else para dar dicas ao usuário: "Muito alto", "Muito baixo" ou "Parabéns!"."""

n_secreto = 42 

palpite = 0

print (" Tente adivinhar um numero entre 1 e 100: ")

while  palpite != n_secreto :
     
    try:
        entrada = input("Seu palpite: ")
        palpite = int(entrada)
       
        if palpite < n_secreto:
            print(" Muito baixo, tente um numero maior ")
        elif palpite > n_secreto and palpite < 101:
            print(" Muito alto, tente um numero menor ")
        elif palpite > 100:
            print("Por favor digite apenas numeros inteiros entre 1 e 100")    
        else:
            print(f"Parabéns você acertou o numero secreto {n_secreto}")
    except ValueError:
        print("Por favor digite apenas numeros inteiros entre 1 e 100")
        


