# Crie uma função chamada analisar_texto(texto) que:
# Recebe um texto (string) como parâmetro.
# Retorna:
# Quantas palavras tem (split() e len()).
# Quantas letras tem (desconsidere espaços).
# Quantas vezes a letra “a” aparece.

def analisar_texto(frase):
    palavras = len(frase.split())
    letras = len(frase.replace(" ", ""))
    a = frase.lower().count("a")
    return palavras, letras, a

frase = "é isso guys"
qtd_palavras, letras, a = analisar_texto(frase)

print(f"Palavras: {qtd_palavras}")
print(f"Letras: {letras}")
print(f"Ocorrências de 'a': {a}")