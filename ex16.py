''' Estudo de caso:
Você foi contrato pelo exercíto brasileiro
para desenvolver um sistema de alistamento
militar, onde se le o ano de nascimento
do candidato e o genero, o sistema irá calcular
a idade, 
se a idade for maior igual a 18 e o sexo masculino
ele estará apto a se alistar, senão não apto
'''


nasc = int(input("Digite o ano que voce nasceu (aaaa) "))
genero = input("digite seu genero (M ou F)").upper()

idade = 2025 - nasc

if ( idade >= 18 and genero == "M"):
    print(f"Você tem {idade} anos  e está apto a se alistar ")
else :
    print("voce não está apto ")   
