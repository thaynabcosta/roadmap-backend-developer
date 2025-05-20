# Aprendendo o Básico

## ✍️ Sintaxe Básica

A sintaxe da linguagem de programação Python é o conjunto de regras que define como um programa Python será escrito e interpretado (tanto pelo sistema de execução quanto por leitores humanos)

### Regras

Identificadores podem ser escritos com uma combinação de letras em lowercase (a até z) ou uppercase (A até Z) ou dígitos (0 até 9) ou um underline (_). Nomes como minhaClasse, variavel_1 e minha_variavel são exemplos válidos de identificadores.

Variáveis são case sensitive (idade, Idade e IDADE são três variáveis diferentes) Identificadores não podem começar com dígitos: 13variavel é inválido, porém variavel13 é aceito!

Palavras-chave jamais podem ser usadas como identificadores!

### Indentação

Enquanto em outras linguagens de programação a indentação é usada apenas para tornar o código mais legível, em Python ela é importantíssima, Python usa a indentação para indicar blocos de código, por exemplo:

```bash
vida = 100
if vida > 0:
   print("Você está vivo")
```

Caso você não utilize a indentação correta, Python irá disparar um erro.

### Comentários
Python tem a capacidade de comentários para que seja mais fácil de lermos os códigos de outros programadores, melhora muito a comunicação!

Comentários começam com #, por exemplo:

```bash
# Este é um comentário  

print("Códigos comentados são muito mais fáceis de serem compreendidos")
```

Python também suporta docstrings, que são comentários que podem extender até mais linhas, veja:

```bash
"""
Este é um comentário
que abrange várias 
linhas do programa
"""
print("Procure sempre comentar o seu código")
```

### Statements
As instruções em Python geralmente terminam com uma nova linha. Python, entretanto, permite o uso do caractere de continuação de linha (\) para indicar que a linha deve continuar. Por exemplo:

```bash
total = 3 + \
    5 + \
    7
print(total) # 15
```

O ponto e vírgula (;) permite várias instruções em uma única linha, visto que nenhuma instrução inicia um novo bloco de código. Aqui está uma amostra que ilustra esta ideia:

```bash
x, y = 9, 3; z = x * y; print(f'{x} x {y} = {z}')
# 9 x 3 = 27
```

## Variáveis e Tipos de Dados

Python é uma linguagem dinamicamente tipada, ou seja, você não precisa declarar o tipo da variável; o interpretador cuida disso. O tipo da variável pode até mudar durante a execução do programa.

### Tipos de Dados Básicos 

- int — números inteiros (ex: 10, -5, 0)  
- float — números decimais/ponto flutuante (ex: 3.14, 1.0)  
- complex — números complexos com parte real e imaginária (ex: 5+2j)  
- str — strings, textos (ex: "Python", 'Bia')  
- bool — booleanos, True ou False  
- list — listas mutáveis, podem conter elementos de vários tipos (ex: [1, 2, "a"])
- tuple — tuplas imutáveis, parecidas com listas mas não podem ser modificadas depois  
- dict — dicionários, estrutura chave:valor (ex: {"nome": "Bia", "idade": 24})

### Exemplos Rápidos

```bash
idade = 24           # int
altura = 1.75        # float
nome = "Bia"         # str
ativo = True         # bool
notas = [8.5, 9.0]   # list
ponto = (10, 20)     # tuple
dados = {"id": 1}    # dict
```

### Conversão de tipos (casting)
Você pode converter tipos facilmente, por exemplo:

```bash
altura = 1.80
altura_str = str(altura)    # float para str

idade = 24
idade_float = float(idade)  # int para float

ativo = True
ativo_int = int(ativo)     # bool para int (True vira 1, False vira 0)
```

### Erros Comuns

- TypeError: ocorre quando você tenta operar entre tipos incompatíveis, por exemplo, somar string com número.  

```bash
peso = 65.5
altura = "1.7"
imc = peso / altura**2  # ERRO: não dá para calcular com str
```

- Solução: converta para o tipo correto antes de operar.  

```bash
altura = float(altura)
imc = peso / altura**2
```

## Condicionais(If, Else, Elif)

O que são?  
- Estruturas condicionais controlam o fluxo do programa, decidindo qual bloco de código será executado com base em condições lógicas.  

Por que usar?  
- Para executar comandos diferentes dependendo do valor de variáveis, evitando erros e tornando o programa flexível.  

### Sintaxe 

```bash
if condição:
    # bloco executado se condição for verdadeira
else:
    # bloco executado se condição for falsa
```

### Exemplo simples

```bash
idade = 18
if idade >= 16:
    print("Pode tirar título de eleitor")
else:
    print("Não precisa de título de eleitor")
```

Como funciona?  
O if testa uma condição (ex: idade >= 16).  
Se for verdadeira, executa o bloco indentado abaixo do if.  
Se for falsa, executa o bloco indentado no else (se houver).  
Você pode adicionar mais condições com elif.  

### Exemplo com elif
```bash
cor = "amarelo"

if cor == "verde":
    print("Acelerar")
elif cor == "amarelo":
    print("Atenção")
else:
    print("Parar")
```

### Importante sobre indentação

No Python, a indentação define quais comandos pertencem a cada bloco condicional. Sem ela, o código dá erro ou não funciona direito.

Operadores comuns em condições:

- Igualdade: ==  
- Diferença: !=  
- Maior que: >  
- Menor que: <  
- Maior ou igual: >=  
- Menor ou igual: <=  
- Teste lógico: and, or, not

## Loops

### 📌 1. O que são Loops (ou Estruturas de Repetição)?

São blocos de código que executam repetidamente enquanto uma condição for verdadeira ou até acabar uma sequência de dados.
No Python, temos dois principais tipos:  

- for
- while

### 🔁 2. Loop for

Usado para iterar sobre elementos de uma sequência (listas, tuplas, strings, dicionários, etc).

Sintaxe:
```bash
for variavel in iteravel:
    # bloco de código
```

Exemplo com lista:
```bash
lista = [1, 2, 3]
for item in lista:
    print(item)
```

*for...else*  
Permite executar um bloco final após o loop ser completado (sem break).
```bash
for item in lista:
    print(item)
else:
    print("Loop finalizado com sucesso.")
```

### 🔁 3. Loop while

Executa enquanto uma condição for verdadeira.  
Sintaxe:

```bash
while condicao:
    # bloco de código
```
Exemplo:

```bash
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

*while...else*  
Roda o bloco else se o loop terminar normalmente (sem break).

### 🛠️ 4. Funções Auxiliares

range(start, stop, step)  
Gera uma sequência de números.

```bash
for i in range(3):
    print(i)  # 0, 1, 2
enumerate(iteravel)
```

*enumerate(iteravel)*  
Retorna índice e valor ao iterar.

```bash
for i, valor in enumerate(['a', 'b']):
    print(i, valor)
``` 

### ⚠️ 5. Comandos de Controle

- break: interrompe o loop imediatamente.  
- continue: pula a iteração atual e continua o loop.  
- pass: ignora a instrução atual (usado como placeholder).  

Exemplo com *break*:
```bash
for i in range(10):
    if i == 5:
        break
    print(i)
```

## Referências

[Sintaxe](https://pythoniluminado.netlify.app/sintaxe)  
[PEP 8](https://peps.python.org/pep-0008/)  
[Tipos de Variáveis disponíveis no Python](https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python)  
[Estruturas Condicionais no Python](https://www.hashtagtreinamentos.com/estruturas-condicionais-no-python?gad_source=1&gad_campaignid=14380361989&gbraid=0AAAAADLlh88YmRgAAIwFuyNv1YaArfjU9&gclid=CjwKCAjwravBBhBjEiwAIr30VITs5Yu4YR1PjfTwTwAxDh_jbP_WdpExxhlkSXBttZNkJWmoonYPBRoCDZMQAvD_BwE)  
[Loops e Estruturas de Repetição no Python](https://pythonacademy.com.br/blog/estruturas-de-repeticao)