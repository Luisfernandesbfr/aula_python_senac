'''usando  loop while para solicitar ao usuário que digite um número maior
 que 10 
 Repita enquanto o 
número for menor 
ou igual a 10.
'''
n = 0

#solicitar ao usuário que digite um número maior que 10
print("--- Digite um Número Maior que 10 ---")

#Usando um loop while para garantir que o número seja maior que 10
while n <= 10:
    try:
        # pedindo ao usuário para digitar um número maior que 10
        entrada = input("Por favor, digite um número maior que 10: ")
        n = int(entrada)
        
       #Verificando se o número é maior que 10
        if n <= 10:
            print(f"O número {n} não é maior que 10. Tente novamente.")
    #Tratando erro de valor inválido
    except ValueError:
       
        print(f"'{entrada}' não é um número válido. Por favor, digite um número inteiro.")
      #Incrementando o contador
        numero = 0