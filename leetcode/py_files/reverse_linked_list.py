# Node - объект, который добавляем в список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def printValue(self):
        print(self.data)

# объект для самого списка
class LinkedList:
    def __init__(self, node):
        self.head = node # first element in list

    def insert_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def __repr__(self):
        s = ''
        tmp = self.head
        while tmp:
            s = s + str(tmp.data)
            tmp = tmp.next
        return s

# создали связанный список
ll = LinkedList(Node(1))
ll.insert_at_beginning(Node(2))
ll.insert_at_beginning(Node(3))

print(ll)

# Задача: развернуть связанный список
## обычное решение
def print_in_reverse(head):
    arr = []
    tmp = head
    while tmp:
        arr.append(tmp)
        tmp = tmp.getNext()

    for el in arr[::-1]:
        el.printValue()


## решение через рекурсию
def print_in_reverse_rec(head):
    if not head.getNext():
        head.printValue()
        return
    else:
        print_in_reverse_rec(head.getNext())
    head.printValue()
    return

print_in_reverse_rec(ll.head)



