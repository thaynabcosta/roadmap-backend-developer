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

## Referências


[Python Arrays](https://www-w3schools-com.translate.goog/python/python_arrays.asp?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)  
[Python Linked Lists](https://www-geeksforgeeks-org.translate.goog/python-linked-list/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)
[Estruturas de Dados — Pilha, Fila e Heap](https://medium.com/mlworks/data-structures-stack-queue-and-heap-793f4d4d73e6)
[Binary Search Tree In Python](https://www.geeksforgeeks.org/binary-search-tree-in-python/)