# Crie uma lista com 5 elementos.
# Peça para o usuário informar o índice do item que ele quer visualizar.
# Trate o erro de índice inválido (IndexError) e de tipo inválido (ValueError).

cores = ["Azul", "Verde", "Vermelho", "Amarelo", "Rosa"]

try:
    indice_desejado = int(input("Digite o índice que deseja acessar na lista de cores: "))
    print(cores[indice_desejado])
except ValueError:
    print("Valor inserido inválido.")
except IndexError:
    print("Índice inexistente.")

