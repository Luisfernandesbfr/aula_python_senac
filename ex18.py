''' Desenvolva um código python que leia um cargo de 
funcionário, de acordo com o cargo mostre o saláro
vide tabela abaixo.
caixa-1500
vendedor-2400
gerente-4000
de acordo com os salários acima , calcule:
inss = 12% sobre o salário
irrf se o salário for maior que 2000 o irrf será de 14% 
sobre o salário senão será de 8%
salário final = salario - irrf - inss

'''

cargo = input("Digite o seu cargo: ").upper()

sal_base_caixa = 1500
sal_base_vendedor = 2400
sal_base_gerente = 4000
sal_final_caixa = sal_base_caixa - sal_base_caixa * 0.12 - sal_base_caixa * 0.08 
sal_final_vendedor = sal_base_vendedor - sal_base_vendedor * 0.12 - sal_base_vendedor * 0.14
sal_final_gerente = sal_base_gerente - sal_base_gerente * 0.12 - sal_base_gerente * 0.14


if (cargo == "CAIXA" ):
    print (f"o seu salario final é {sal_final_caixa} " )

elif( cargo == "VENDEDOR"):
    print(f"o seu salario final é {sal_final_vendedor}")
elif ( cargo == "GERENTE") :
    print(f"o seu salario final é {sal_final_gerente}")
else :
    print("Cargo não encontrado")               
