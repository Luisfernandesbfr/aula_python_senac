'''Desenvolva um codigo que leia 3 numeros 
e mostre o maior '''


v1 = int(input("Digite um valor: "))
v2 = int(input("Digite um valor: "))
v3 = int(input("Digite um valor: "))


if (v1 > v2 and v1 > v3):
    print(f"O maior numero entre {v1} {v2} {v3} é o {v1}")
elif (v2 > v1 and v2 > v3):
    print (f"O maior numero entre {v1} {v2} {v3} é o {v2}")
else :
    print (f"O maior numero entre {v1} {v2} {v3} é o {v3}")    
