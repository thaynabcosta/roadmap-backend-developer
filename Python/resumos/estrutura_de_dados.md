# Estrutura de Dados

## Arrays

### ✅ O que é um array?

Um array é uma variável composta: ele armazena vários valores ao mesmo tempo.  
Pense em uma caixa de ovos: uma variável comum guarda 1 ovo. Um array guarda vários ovos em uma mesma caixa.

### 🧠 Por que usar arrays?

- Quando você precisa armazenar vários dados relacionados (ex: notas de uma turma, temperaturas do mês, etc.).  
- Quando quer fazer operações matemáticas em massa (ex: somar todos os valores, multiplicar por 2, etc.).

### 📌 Lista vs. Array em Python

| Característica          | Lista (`list`)                       | Array (`array` ou `np.array`)               |
| ----------------------- | ------------------------------------ | ------------------------------------------- |
| Tipo de dados           | Pode misturar tipos (int, str, etc.) | Tipos iguais (todos int, todos float...)    |
| Flexibilidade           | Muito flexível                       | Mais restrito, mas mais rápido para números |
| Usos comuns             | Qualquer estrutura de dados          | Cálculos numéricos intensivos               |
| Biblioteca padrão       | Nativa no Python (`list`)            | `array` vem do módulo `array` ou do `NumPy` |
| Performance com números | Mediana                              | Alta (especialmente com `NumPy`)            |

### ⚙️ Exemplo com list (nativa)

```bash
notas = [7.5, 8.0, 9.2, 6.5]
print(notas[2])  # Acessa o terceiro elemento → 9.2
notas.append(10) # Adiciona uma nota
```
- Permite tipos misturados:

```bash
dados = [1, 'oi', 3.14, True]
```

### ⚙️ Exemplo com array (módulo array)

```bash
from array import array
numeros = array('i', [1, 2, 3, 4])  # 'i' = inteiro
print(numeros[1])  # Saída: 2
```

### ⚙️ Exemplo com NumPy (mais comum para arrays numéricos)

```bash
import numpy as np
valores = np.array([1, 2, 3, 4])
print(valores * 2)  # Multiplica todos os elementos
```

### 🧠 Quando usar lista?

- Quando você quer armazenar dados variados.  
- Quando não precisa de performance.

### 🧠 Quando usar array/NumPy array?

- Quando vai fazer muitos cálculos numéricos.  
- Quando precisa de eficiência e velocidade.

## Linked Lists

### 📌 O que é uma Linked List?

É uma estrutura de dados linear composta por nós (nodes), onde cada nó contém dois elementos:

- Valor (dados)  
- Referência para o próximo nó (ponteiro)

👉 Diferente de listas nativas do Python (list), a Linked List não usa índices e não armazena os dados em blocos contínuos de memória. Isso a torna eficiente para inserções e deleções dinâmicas.

### 🧱 Como é um nó (Node)?

```bash
class Node:
    def __init__(self, data):
        self.data = data  # valor armazenado
        self.next = None  # ponteiro para o próximo nó
```
### 🧵 Como funciona a lista ligada?

Você começa com um head (cabeça) que aponta para o primeiro nó. Cada nó aponta para o próximo, até chegar em None, que representa o fim da lista.

### 🛠️ Exemplo básico de Linked List:

```bash
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # se a lista estiver vazia
            self.head = new_node
        else:
            current = self.head
            while current.next:  # percorre até o último nó
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```
### 📚 Operações comuns:

| Operação          | Complexidade | Observação                              |
| ----------------- | ------------ | --------------------------------------- |
| Inserir no início | O(1)         | Simples: só altera o ponteiro da cabeça |
| Inserir no fim    | O(n)         | Precisa percorrer a lista               |
| Remover nó        | O(n)         | Precisa encontrar o nó anterior         |
| Buscar elemento   | O(n)         | Não tem índice, precisa percorrer       |

### ⚔️ Quando usar Linked List?

- Quando há muitas inserções/remoções dinâmicas  
- Quando o custo de realocação de memória (como nas list) for ruim  
- Quando quiser controlar estrutura de dados manualmente

### ❌ Desvantagens:

- Acesso direto é lento (não tem índice)  
- Gasta mais memória (guarda o ponteiro junto com o valor)  
- Difícil de depurar se mal implementado

## Hash Tables

É uma estrutura de dados que armazena pares chave:valor, permitindo acesso super rápido aos dados.  
Em Python, a hash table é implementada pelo tipo dict (dicionário).

### ⚙️ Como funciona internamente?

- Hash Function: transforma a chave em um número (hash).  
- Endereço na memória: esse número é usado como índice para armazenar o valor.  
- Busca eficiente: em vez de procurar item por item, ele vai direto no "endereço".

🔁 Exemplo:
```bash
aluno = {"nome": "Bia", "idade": 25}
print(aluno["nome"])  # Resultado: "Bia"
```

### 🧱 Estrutura

```bash
dicionario = {
    "chave1": "valor1",
    "chave2": "valor2"
}
```

- Chaves podem ser: strings, números, tuplas.  
- Valores podem ser: qualquer coisa.

### 🔥 Vantagens

- Acesso rápido: O(1) para buscar, inserir e deletar.  
- Flexível: aceita qualquer tipo de valor.  
- Leitura intuitiva: muito usado para JSON, APIs, banco de dados, etc.

### ⚠️ Colisões

Quando duas chaves geram o mesmo hash — o Python resolve isso internamente com técnicas como encadeamento. Você não precisa se preocupar no dia a dia.

### 🛠️ Métodos úteis
```bash
d.get("chave", "valor padrão")      # Evita erro se chave não existe
d.keys()                            # Retorna todas as chaves
d.values()                          # Retorna todos os valores
d.items()                           # Retorna (chave, valor) em tuplas
d.pop("chave")                      # Remove a chave e retorna o valor
d.update({"nova_chave": "valor"})  # Atualiza ou adiciona
```
### 💥 Exemplo prático

```bash
estoque = {"banana": 6, "maçã": 4}
estoque["laranja"] = 10  # Adiciona
estoque["banana"] += 2   # Atualiza
del estoque["maçã"]      # Remove
```

### 🧠 Dica de ouro

Use dict quando:  
- Você quer acessar dados rapidamente por uma chave.  
- Precisa de estrutura flexível e dinâmica.

## 📚 Heaps, Stacks (Pilha) e Queues

## Heaps

Metáfora: Pilha de pratos. O último que entra é o primeiro que sai (LIFO – Last In, First Out).  

### ✅ Usos comuns:
- Undo/redo (desfazer/refazer)  
- Recursão  
- Avaliação de expressões (ex: compiladores)  

### 🧠 Conceito:
Inserção e remoção acontecem sempre no topo.

### 🔧 Implementação em Python:
```bash
stack = []
# Push (adicionar)
stack.append(10)
# Pop (remover)
valor = stack.pop()
# Ver o topo
topo = stack[-1]
```

### ⚠️ Observações:

- Simples, eficiente.  
- pop() lança erro se estiver vazia.

## Queue (Fila)

Metáfora: Fila de banco. O primeiro que entra é o primeiro que sai (FIFO – First In, First Out).

### ✅ Usos comuns:

- Processamento em ordem  
- Sistemas de tarefas (ex: prints, downloads)  
- Algoritmos de busca (BFS)

### 🧠 Conceito:

Inserção no fim, remoção no início.

### 🔧 Implementações:

- Usando collections.deque (melhor opção):
```bash
from collections import deque

queue = deque()
# Enqueue
queue.append("A")
# Dequeue
item = queue.popleft()
```

Evite usar listas puras para filas, pois pop(0) é ineficiente (O(n)).

## Heap (Montículo)

Metáfora: Uma árvore binária especial onde o menor (ou maior) valor sempre está no topo.

### ✅ Usos comuns:

- Encontrar mínimo/máximo rapidamente  
- Algoritmos como Dijkstra, A*  
- Gerenciamento de prioridades (ex: filas de prioridade)

### 🧠 Conceito:

Heap mínimo: raiz sempre é o menor.  
Não é ordenado totalmente, só a prioridade de acesso.  

### 🔧 Implementação:

```bash
import heapq

heap = []

# Inserir (heapify automaticamente)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# Remover menor
menor = heapq.heappop(heap)

# Ver menor sem remover
top = heap[0]
```

### ⚠️ Observações:

- O heapq usa listas, mas mantém a propriedade do heap.
- Para max heap, insira números negativos ou use heapq._heapify_max() (não recomendado em produção).

### ⚔️ Comparativo rápido:

| Estrutura | Ordem de Acesso | Quando Usar                       | Complexidade     |
| --------- | --------------- | --------------------------------- | ---------------- |
| Stack     | LIFO            | Quando precisa desfazer ações     | O(1)             |
| Queue     | FIFO            | Processamento em ordem de chegada | O(1) com `deque` |
| Heap      | Prioridade      | Sempre pegar o menor/maior valor  | O(log n)         |

## Binary Search Tree

### 🌳 O que é uma Binary Search Tree (BST)?

É uma árvore binária ordenada:
- Cada nó tem no máximo dois filhos: esquerdo e direito.  
- Regra:  
    - Filho esquerdo < nó atual  
    - Filho direito > nó atual

### ✅ Pra que serve?

- Buscar dados rapidamente (log n se balanceada)  
- Inserir/remover de forma estruturada  
- Estrutura base de várias outras (ex: AVL, Red-Black, B-trees)  
- Ideal pra criar dicionários, índices, autocomplete, etc.

### 🧠 Conceitos-Chave

| Operação | O quê faz?                      | Tempo (ideal: árvore balanceada) |
| -------- | ------------------------------- | -------------------------------- |
| Inserção | Adiciona valor mantendo a ordem | O(log n)                         |
| Busca    | Procura valor                   | O(log n)                         |
| Remoção  | Remove valor e reorganiza       | O(log n)                         |

### ⚙️ Implementação básica em Python

```bash
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, nodo, valor):
        if nodo is None:
            return Node(valor)
        if valor < nodo.valor:
            nodo.esquerda = self._inserir_recursivo(nodo.esquerda, valor)
        elif valor > nodo.valor:
            nodo.direita = self._inserir_recursivo(nodo.direita, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.esquerda, valor)
        else:
            return self._buscar_recursivo(nodo.direita, valor)

    def em_ordem(self):  # para ver os dados ordenados
        self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, nodo):
        if nodo:
            self._em_ordem_recursivo(nodo.esquerda)
            print(nodo.valor)
            self._em_ordem_recursivo(nodo.direita)
```

### 🧪 Exemplo de uso:

```bash
arvore = BST()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)

arvore.em_ordem()  # Saída: 20 30 40 50 70

print(arvore.buscar(40))  # Retorna o Node com valor 40
print(arvore.buscar(100)) # Retorna None
```

### ⚠️ Limitações:

- BST desbalanceada pode virar uma lista encadeada (O(n))  
- Solução: usar árvores balanceadas (AVL, Red-Black Tree)

## Recursion

### 🔁 O que é recursão?

É quando uma função chama a si mesma para resolver um problema dividido em partes menores.

### Exemplo mental:

Quer saber o fatorial de 5?  
Você resolve assim:
```bash
5! = 5 × 4!
4! = 4 × 3!
...
1! = 1
```

### 🧠 Estrutura básica da recursão:

```bash
def funcao(param):
    if condição_base:
        return resultado_simples
    else:
        return funcao(param_menor)
```

### ⚠️ Duas partes essenciais:

- Condição de parada (caso base) → SEM ISSO, vira loop infinito.  
- Chamada recursiva com input reduzido → pra ir se aproximando da parada.

### ✅ Quando usar recursão?

Use quando o problema:  
- Pode ser quebrado em subproblemas iguais  
- Tem uma estrutura repetitiva que depende do passo anterior  
- Envolve árvores, grafos, backtracking, etc.
- Exemplos:  
    - Fatorial  
    - Fibonacci  
    - Percorrer árvores (DFS)  
    - Resolver labirintos  
    - Permutações, combinações

### 🔧 Exemplo 1: Fatorial

```bash
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
fatorial(5) → 5 × 4 × 3 × 2 × 1 = 120
```

### 🔧 Exemplo 2: Fibonacci

```bash
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(5) → 5 (0, 1, 1, 2, 3, 5)
```

*⚠️ Essa versão é lenta (recalcula muita coisa). Otimize com memoization ou programação dinâmica.*

### ❌ Erros comuns:

- Esquecer o caso base → crasha com RecursionError  
- Caso base errado → loop infinito ou resultado incorreto  
- Usar recursão onde loop seria mais simples e eficiente

### 🧪 Recursion vs Loop
| Situação                                      | Melhor usar |
| --------------------------------------------- | ----------- |
| Cálculo simples, repetitivo                   | Loop        |
| Estruturas recursivas (árvores, grafos)       | Recursão    |
| Resolver problema quebrando em partes menores | Recursão    |


### 🚨 Limite de Recursão em Python

Python tem um limite padrão de recursão máxima (geralmente 1000).  
Se passar disso:

```bash
RecursionError: maximum recursion depth exceeded
```
Pode aumentar com:
```bash
import sys
sys.setrecursionlimit(2000)
```

Só use isso se sabe o que está fazendo. Recursão profunda pode quebrar seu programa com stack overflow.

## Sorting Algorithmes

### 🧠 O que é "Sorting"?

- É reorganizar uma lista em ordem (crescente ou decrescente).  
- É base pra pesquisa binária, algoritmos de grafos, compressão, bancos de dados, tudo.

### 🔢 Principais Algoritmos de Ordenação:

| Algoritmo      | Complexidade Média | Estável? | In-place? | Quando usar?                                    |
| -------------- | ------------------ | -------- | --------- | ----------------------------------------------- |
| Bubble Sort    | O(n²)              | Sim      | Sim       | Ensino, não usar na prática                     |
| Insertion Sort | O(n²)              | Sim      | Sim       | Pequenas listas já quase ordenadas              |
| Selection Sort | O(n²)              | Não      | Sim       | Simples, mas ineficiente                        |
| Merge Sort     | O(n log n)         | Sim      | Não       | Dados grandes onde a estabilidade importa       |
| Quick Sort     | O(n log n)         | Não      | Sim       | Rápido na prática, exceto dados quase ordenados |
| Heap Sort      | O(n log n)         | Não      | Sim       | Usa heap, bom para espaço limitado              |
| TimSort        | O(n log n)         | Sim      | Sim       | Usado internamente em Python (`sorted()`)       |

### 🔍 Explicação Rápida de Cada Um:

### Bubble Sort

- Compara pares adjacentes e troca se estiverem fora de ordem.
- Repetição até estar ordenado.

```bash
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

Lento demais. Evita na prática.

### Insertion Sort

Vai pegando cada item e inserindo no lugar certo da parte já ordenada.

```bash
def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = chave
```
Bom pra listas pequenas ou quase ordenadas.

### 🎯 Selection Sort

Seleciona o menor elemento e coloca na posição correta.

```bash
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

Simples, mas ineficiente e não estável.

### 🔀 Merge Sort

Divide a lista em partes, ordena cada uma e combina de volta ordenado.

```bash
def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        arr[k:] = esquerda[i:] + direita[j:]
```

Estável, ótimo desempenho. Usa mais memória.

### ⚡ Quick Sort

Escolhe um pivô, separa menor e maior, ordena recursivamente.

```bash
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivô = arr[0]
    menores = [x for x in arr[1:] if x <= pivô]
    maiores = [x for x in arr[1:] if x > pivô]
    return quick_sort(menores) + [pivô] + quick_sort(maiores)
```

Muito rápido, mas ruim se os dados já estão quase ordenados (pior caso O(n²)).

### 🛠️ Heap Sort

Constrói um heap (estrutura de árvore) e extrai o menor/maior.

```bash
import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
```

Ótimo para grandes volumes e consumo de memória controlado. Não estável.

### 🐍 TimSort (O que o Python usa internamente)

```bash
sorted(lista)
lista.sort()
TimSort = Merge Sort + Insertion Sort inteligente.
```

Muito rápido, estável, funciona bem com qualquer tipo de dado real.

### 🚀 Qual usar na prática?

| Situação                            | Algoritmo            |
| ----------------------------------- | -------------------- |
| Lista pequena ou quase ordenada     | Insertion Sort       |
| Dados grandes, estabilidade importa | Merge Sort           |
| Desempenho puro, sem estabilidade   | Quick Sort           |
| Pouca memória disponível            | Heap Sort            |
| Na vida real, em Python             | `sorted()` (TimSort) |


## Referências

[Python Arrays](https://www-w3schools-com.translate.goog/python/python_arrays.asp?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)  
[Python Linked Lists](https://www-geeksforgeeks-org.translate.goog/python-linked-list/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)
[Estruturas de Dados — Pilha, Fila e Heap](https://medium.com/mlworks/data-structures-stack-queue-and-heap-793f4d4d73e6)
[Binary Search Tree In Python](https://www.geeksforgeeks.org/binary-search-tree-in-python/)
[Python Function Recursion](https://www.w3schools.com/python/gloss_python_function_recursion.asp)