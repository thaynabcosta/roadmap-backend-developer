# Crie uma agenda semanal, onde a chave é o dia da semana e o valor é a atividade principal.
# Faça uma função que atualize a atividade de um dia específico.
# Faça outra função que imprima os dias e atividades.

def atualizar_agenda(agenda, chave, valor):
    agenda[chave] = valor

def ver_agenda(dic):
    print("Dia da Semana | Treino")
    for chave, valor in dic.items():
        print(chave + "|" + valor)

def cabecalho_agenda():
    print("######################################################")
    print("        C R O N O G R A M A   T R E I N O             ")
    print("######################################################")


cronograma_treino = {
    "Segunda": "Perna",
    "Terça": "Peito",
    "Quarta": "Costas",
    "Quinta": "Ombro",
    "Sexta": "Perna",
    "Sábado": "Braço",
    "Domingo": "Day off" 
}


if __name__ == "__main__":

    cabecalho_agenda()
    ver_agenda(cronograma_treino)

    atualizar_agenda(cronograma_treino, "Sábado", "Cardio")
    print("\n>>> Atualizando sábado para Cardio...\n")

    cabecalho_agenda()
    ver_agenda(cronograma_treino)

