class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def adicionar(self, value):
        novo_no = Node(value)
        if self.head is None:
            self.head = novo_no
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = novo_no
    
    def imprimir(self):
        count = 0
        atual = self.head
        while atual:
            print(atual.value)
            atual = atual.next
            count += 1
        print(f"Quantidade de nós: {count}")

lista_frutas = LinkedList()
lista_frutas.adicionar("banana")
lista_frutas.adicionar("uva")
lista_frutas.adicionar("maçã")
lista_frutas.imprimir()