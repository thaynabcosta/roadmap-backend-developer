# Percorrendo dados
# Cenário: Você tem uma lista de alunos e porcentagem de presença. Precisa identificar quem pode receber certificado.
# Tarefa: Escreva um for que percorra a lista e diga quem recebe o certificado.
# Desafio extra: Crie uma nova lista chamada aprovados com apenas os nomes de quem foi aprovado.

alunos = [
    {"nome": "Bia", "idade": 24, "presenca": 90},
    {"nome": "Léo", "idade": 15, "presenca": 100},
    {"nome": "Ana", "idade": 18, "presenca": 60},
]

aprovados = []

for aluno in alunos:
    if aluno["idade"] >= 16 and aluno["presenca"] >= 75:
        aprovados.append(aluno["nome"])
    else:
        print(f"{aluno["nome"]} não pode receber o certificado!")

print(f"Lista dos aprovados: {aprovados}")