nota = 0

while nota >= 0 and nota <= 10 :
    try:
        nota = int(input("Digite uma nota entre 0 e 10 : "))
        print("Nota valida")
    except ValueError:
        print("Entrada invalida. Por favor, digite um numero inteiro")

print (f"Nota invalida registrada: {nota}")         