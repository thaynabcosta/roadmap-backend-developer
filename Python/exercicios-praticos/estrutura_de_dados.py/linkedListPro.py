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

    def remover(self, value):
        atual = self.head
        anterior = None
        while atual:
            if atual.value == value:
                if anterior is None:
                    self.head = atual.next
                else:
                    anterior.next = atual.next
                return
            anterior = atual
            atual = atual.next

    def inserir_na_posicao(self, value, posicao):
        novo_no = Node(value)

        if posicao == 0:
            novo_no.next = self.head
            self.head = novo_no
            return

        atual = self.head
        index = 0

        while atual and index < posicao - 1:
            atual = atual.next
            index += 1

        if atual is None:
            print("Posição fora dos limites.")
            return

        novo_no.next = atual.next
        atual.next = novo_no

        


lista_frutas = LinkedList()
lista_frutas.adicionar("banana")
lista_frutas.adicionar("uva")
lista_frutas.adicionar("maçã")
lista_frutas.imprimir()
lista_frutas.remover("uva")
lista_frutas.imprimir()
lista_frutas.inserir_na_posicao("laranja", 1)
lista_frutas.imprimir()