# Regras de 

# Cenário: No sistema do curso, você precisa decidir se a pessoa pode receber certificado:
# Só recebe se tiver mais de 75% de presença e for maior de 16 anos.
# Escreva a lógica para verificar se a pessoa recebe certificado.

nome = input("Nome:")
idade = int(input("Idade:"))
presenca_percentual = int(input("Percentual de presença: "))

if idade >= 16 and presenca_percentual >= 75:
     print(f"Certificado liberado para {nome}")
else:
    print(f"Certificado não liberado para {nome}")