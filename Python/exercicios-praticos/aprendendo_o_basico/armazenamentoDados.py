# Exercício Prático 2: Armazenando dados
# Tarefa: Crie variáveis para representar essas informações para 1 pessoa, considerando tipos adequados.

nome = str(input("Nome: "))
idade = int(input("Idade: "))
presenca = str(input("Presença: ")).strip().lower() == "sim"

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Presença: {presenca}")

print(f"{nome} tem {idade} anos")