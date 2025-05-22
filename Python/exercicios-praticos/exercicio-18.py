#Desafio Bônus – Misturando Tudo
#Crie um programa que:
#Solicita ao usuário 5 nomes e armazena numa lista.
#Remove nomes duplicados usando um set.
#Ordena os nomes em ordem alfabética.
#Armazena o resultado final como uma tupla e imprime.

nomes = []

for i in range(0,5):
    nome = input("Digite uma nome: ")
    nomes.append(nome)

nomes = set(nomes) #remover duplicidades
nomes = list(nomes) #transaformado em lista para tornar mutável 
nomes.sort() # ordenar em ordem alfabética
nomes = tuple(nomes) #transformar em tupla

print(nomes)