class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


lista = [1, 2, 3, 5]

no1 = Node(1)
no2 = Node(2)
no3 = Node(3)
no4 = Node(5)

no1.next = no2
no2.next = no3
no3.next = no4

no_atual = no1
while no_atual is not None:
    print(no_atual.value)
    no_atual = no_atual.next
