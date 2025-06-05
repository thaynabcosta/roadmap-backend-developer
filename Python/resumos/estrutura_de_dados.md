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

## Referências


[Python Arrays](https://www-w3schools-com.translate.goog/python/python_arrays.asp?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)  

