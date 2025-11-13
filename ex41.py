

def somar (a,b):
    return a+b

def subtrair (a,b):
    return a-b

def multi (a,b):
    return a*b

def div (a,b):
    if b != 0:
        return  a / b
    else:
        print("valor invalido")  
escolha = ""         
while escolha != "0":
    escolha = input("Digite uma opção \n 1- Somar \n 2- Subtrair \n 3- Multiplicar \n 4- Dividir \n Digite 0 para sair \n ")

    num1=int(input("Digite o primeiro numero : "))
    num2=int(input("Digite o segundo numero : "))
    if escolha == "1":
        x = somar(num1,num2)
    elif escolha == "2":
        x = subtrair(num1,num2)
    elif escolha == "3":
        x = multi(num1,num2)
    elif escolha == "4":
        x = div(num1,num2)        
    else:
        break        

    print(f"O resultado da operação é {x} \n")