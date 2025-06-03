class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def imprimir_no(valor_inicial):
    no_atual = valor_inicial
    qntd_nos = 0
    while no_atual is not None:
        print(no_atual.value)
        no_atual = no_atual.next
        qntd_nos += 1
    print(f"Quantidades de nós: {qntd_nos}")

fruta1 = Node("maçã")
fruta2 = Node("banana")
fruta3 = Node("uva")

fruta1.next = fruta2
fruta2.next = fruta3

imprimir_no(fruta1)
