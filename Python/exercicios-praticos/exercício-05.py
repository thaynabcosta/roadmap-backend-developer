# Escreva um programa que:
# 1. Recebe a idade do usuário como string (input)
# 2. Converte para inteiro
# 3. Verifica se pode dirigir (idade >= 18)
# 4. Exibe uma mensagem formatada com a idade e o resultado

idade = input("Digite sua idade: ")

idade = int(idade)

if idade >= 18:
    print(f"Você tem {idade}. Portanto, pode dirigir")
else:
    print(f"Você tem {idade}. Portanto, não pode dirigir")