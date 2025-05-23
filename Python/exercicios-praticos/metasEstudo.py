# Crie um dicionário com suas metas de estudo
# Faça uma função ver_status(dicionario) que imprima

def ver_status(dic):
    for chave, valor in dic.items():
        print(f"Tópico: {chave} -> Status: {valor}")

def exibicao_cabecalho():
    print("####################################################")
    print("      E X I B I Ç Ã O   D O S   S T A T U S         ")
    print("####################################################")

estudos = {
    "Dicionários": "Em progesso",
    "Módulos": "Pendente",
    "Lambdas": "Pendente",
    "Decorators": "Pendente",
    "Iterators": "Pendente",
    "Regular Expressions": "Pendente"
}

if __name__ == "__main__":

    exibicao_cabecalho()
    ver_status(estudos)
