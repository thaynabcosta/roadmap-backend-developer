# Crie uma função verifica_palavra(palavra, lista) que recebe uma palavra e uma lista de palavras.
# A função deve retornar True se a palavra existir na lista, False caso contrário.
# Teste a função com a palavra "banana" e a lista ["maçã", "banana", "laranja"].
# Use a função print() para mostrar o resultado.

def verfica_palavra(palavra_user, lista):
    return palavra_user in lista

frutas = ["maçã", "banana", "laranja"]
palavra_user = input("Digite a palavra desejada: ").lower()

print("A palavra existe dentro da lista? ")
print(verfica_palavra(palavra_user, frutas))
    
    