#Agora quero que você faça outra função:
#analisar_nome(nome), que:
#Receba um nome completo (ex: "Maria da Silva").
#Retorne:
#O nome em MAIÚSCULAS.
#O nome em minúsculas.
#Quantas letras tem sem espaços.
#Quantas letras tem o primeiro nome.

def analisar_nome(nome):
    maiuscula = nome.upper()
    minusculo = nome.lower()
    letras = len(nome.replace(" ", ""))
    divisao_nome = nome.split()
    letras_primeiro_nome = len(divisao_nome[0])
    
    return maiuscula, minusculo, letras, letras_primeiro_nome

nome_user = input("Nome completo: ")

nome_maiusculo, nome_minusculo, qtd_letras, qtd_letras_primeiro_nome = analisar_nome(nome_user)

print(f"Nome maiusculo: {nome_maiusculo}")
print(f"Nome minusculo: {nome_minusculo}")
print(f"Quantidade de letras no nome: {qtd_letras}")
print(f"Quantidade de letras no primeiro nome: {qtd_letras_primeiro_nome}")