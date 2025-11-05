
#Desenvolva um codigo que leia 4 notas, calcule a media e se a media for maior ou igual a 6 imprimir aprovado, senão imprimir Recuperação

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media = (n1+ n2 + n3 + n4) / 4

if (media >= 6):
    print( f" Sua media foi {media} e você está Aprovado ")

else :
    print (f"Sua media foi {media} e você está de Recuperação")    