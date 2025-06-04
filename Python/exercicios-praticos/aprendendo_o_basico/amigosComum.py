#Objetivo: Usar operações de conjuntos.
#Desafio:
#Crie dois conjuntos:
#amigos1 = {"Ana", "Carlos", "João", "Beatriz"}
#amigos2 = {"Carlos", "Mariana", "João", "Fernanda"}
#Encontre:
#Todos os amigos (união)
#Amigos em comum (interseção)
#Amigos exclusivos do grupo 1
#Amigos exclusivos do grupo 2

amigos1 = {"Ana", "Carlos", "João", "Beatriz"}
amigos2 = {"Carlos", "Mariana", "João", "Fernanda"}

print(amigos1 | amigos2)
print(amigos1 & amigos2)
print(amigos1 - amigos2)
print(amigos2 - amigos1)
