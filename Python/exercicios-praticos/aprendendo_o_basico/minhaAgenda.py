# Usa um dicionário para guardar compromissos do dia com hora como chave e tarefa como valor.
# Mostra todos os compromissos ordenados pela hora.

def mostra_agenda(dic):
    for chave, valor in dic.items():
        print(chave + ": " + valor)

agenda = {
    "6 a.m": "Rotina matinal",
    "7 a.m": "Tempo livre",
    "8 a.m": "Arrumar casa",
    "9 a.m": "Tempo livre",
    "10 a.m": "Roadmap Study - Python",
    "12 p.m": "Tempo livre",
    "1 p.m": "Organização dos Estudos",
    "3 p.m": "Tempo livre",
    "4 p.m": "Reconstrução e envio de currículo",
    "6 p.m": "Tempo livre",
    "7 p.m": "Filme",
    "9 p.m": "Tempo livre",
    "10 p.m": "Jogar GTA",
    "11 p.m": "Dormir"
}

print("############################################################")
print("               A G E N D A   D O   D I A                    ")
print("############################################################")

mostra_agenda(agenda)
