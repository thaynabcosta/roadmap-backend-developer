# Peça o nome de um arquivo .txt para o usuário.
# Tente abrir esse arquivo e mostrar o conteúdo.
# Trate FileNotFoundError

try: 
    arquivo = input("Digite o nome do arquivo .txt:")
    with open(arquivo, "r") as f:
        conteudo = f.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado.") 