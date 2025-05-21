# Crie uma função calcula_media(numeros) que recebe uma lista de números.
# A função deve usar a built-in sum() para somar os números e len() para pegar a quantidade.
# Retorne a média (soma dividido pela quantidade).
# Teste a função com a lista [7, 8, 9, 10, 6].
# Imprima o resultado formatado (exemplo: "A média é 8.0").

def calcula_media(num_list):
    media = sum(num_list)/len(num_list)
    return media

notas = [7, 8, 9, 10, 3]
media = calcula_media(notas)

print(f"A média é {media}")