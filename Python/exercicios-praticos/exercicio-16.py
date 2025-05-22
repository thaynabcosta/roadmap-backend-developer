#Desafio:
#Crie uma tupla chamada coordenadas com os valores (15.0, 27.5).
#Tente alterar o primeiro valor para 20.0. O que acontece?
#Transforme a tupla em uma lista, modifique o valor e transforme de volta em tupla.
#Imprima a nova tupla.

tupla_coordenadas = (15.0, 27.5)

#tupla_cordenadas(0) = 20.0 # deu erro 

lista_coordenadas = list(tupla_coordenadas)
lista_coordenadas[0] = 20.0

tupla_coordenadas = tuple(lista_coordenadas)

print(tupla_coordenadas)