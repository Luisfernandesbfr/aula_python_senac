capitais = {
    "Minas Gerais": "Belo Horizonte",
    "Espirito Santo": "Vitória",
    "Parana": "Curitiba",
    "Bahia": "Salvador",
    "Pernambuco": "Recife"
}

print("--- Capitais Cadastradas ---")
for chave, valor in capitais.items():
    print(f"{valor}")

consulta_estado = input("Digite o nome de um estado para ver sua capital (Ex: Bahia): ").strip()

if consulta_estado:
    capital_encontrada = capitais[consulta_estado]
    print(f"A capital de **{consulta_estado}** é **{capital_encontrada}**.")
else:
    print(f"O estado '**{consulta_estado}**' não foi encontrado no dicionário.")

