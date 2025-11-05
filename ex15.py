''' Desenvolva um código python que verifique se
a temperatura esta frio, agradável ou calor,
siga a tabela abaixo
menor que 18 - frio
entre 18 e 30 - agradavel
maior que 30 calor'''


t = float(input("Digite a temperatura => "))

if (t < 18):
    print( " Está frio !")
elif (t >=18 and t <= 30 ):
    print("Está agradavel !")
else:           
    print("Está calor ! ")