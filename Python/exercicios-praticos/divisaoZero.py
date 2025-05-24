#Crie um programa que:
#1. Peça dois números ao usuário.
#2. Divida o primeiro pelo segundo.
#3. Trate ZeroDivisionError e ValueError.

try:
    num_1 = int(input("Digite um valor: "))
    num_2 = int(input("Digite outro valor: "))

    divisao = num_1+num_2

    print(divisao)
    
except ZeroDivisionError:
    print("Não é possivel divisão por zero.")
except ValueError:
    print("Valor inserido é inválido.")