# Receba dois números do usuário, converta para float e imprima:
# A soma
# A média
# Se os dois números são iguais

numero_um = int(input("Digite o valor 1: "))
numero_dois = int(input("Digite o valor 2: "))

numero_um, numero_dois = float(numero_um), float(numero_dois)

soma = numero_um + numero_dois
media = soma/2

if numero_um == numero_dois:
    equidade = "são iguais"
else:
    equidade = "não são iguais"

print(f"A soma dos valores é {soma}. A média é {media}. E os valores {equidade}.")
