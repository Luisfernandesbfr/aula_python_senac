#Desenvolver um codigo que peça 2 numeros e imprima o maior 


n1 = int(input("Digite um numero:"))
n2 = int(input("Digite um numero:"))
if(n1 > n2):
    print(f"o maior numero é o {n1}")
elif (n1 == n2):
    print(f"os numeros {n1} e {n2} são iguais")    
else:
     print(f"o maior numero é o {n2}")    