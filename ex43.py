

def e_par (numero):
    return numero % 2 == 0

num =  int(input("Digite um numero inteiro : "))

resultado = e_par(num)

if resultado :
    print(f"o numero {num} é par ")
else:
    print(f"o numero {num} é impar ")    