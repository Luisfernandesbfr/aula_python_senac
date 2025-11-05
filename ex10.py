#Desenvolver um codigo que leia 2 nomes, se o primeiro nome for senac ou o segundo nome for cinelandia, imprimir SENAC
#senão, imprimir não é senac

nome = input ("Digite o primeiro nome:")
nome2 = input ("Digite o segundo nome:")
nome = nome.lower()
nome2 = nome2.lower()
if (nome == "senac" or nome2 == "cinelandia"):
    print(f"Seja bem vindo {nome} {nome2}")
else:
    print ("Você não é SENAC")  