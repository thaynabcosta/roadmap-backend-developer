# Objetivo: Criar, modificar e manipular uma lista.
# Desafio:
# Crie uma lista chamada compras com os itens: "arroz", "feijão", "ovo", "leite".
# Adicione "café" à lista.
# Substitua "ovo" por "frango".
# Remova "leite" da lista.
# Imprima a lista final.

compras = ["arroz", "feijão", "ovo", "leite"]

compras.append("café")
compras[2] = "Frango"
compras.remove("leite")

print(compras)

