

def maior (a, b):
    if b > a:
      return b
    elif a > b :  
       return a

numero1 = int(input("Digite um numero: "))          
numero2 = int(input("Digite outro numero: ")) 

resultado = maior( numero1,numero2)

print(f"O resultado é {resultado} ")

