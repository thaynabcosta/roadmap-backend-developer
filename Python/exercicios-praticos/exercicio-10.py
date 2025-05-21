# Crie uma função chamada soma que recebe dois números como parâmetros.
# A função deve retornar a soma dos dois números.
# Chame a função e imprima o resultado.
# Extra: Use a função print() do Python para mostrar o resultado.

def soma(a, b):
    return a + b

num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

resultado = soma(num1, num2)

print(f"O resultado da soma entre {num1} e {num2} é {resultado}")