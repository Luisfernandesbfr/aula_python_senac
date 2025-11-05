#Codigo que verifica se um nome  é Senac

nome = input ("Qual o seu nome:")
sobrenome = input ("Qual o seu sobrenome:")
nome = nome.upper()
sobrenome = sobrenome.upper()
if (nome == "SENAC" and sobrenome == "SANTA LUZIA"):
    print(f"Seja bem vindo {nome} {sobrenome}")
else:
    print ("Você não é Senac")    