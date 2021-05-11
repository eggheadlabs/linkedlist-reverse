# How do you reverse a linked list?
# Sample linked-list: 1 -> 2 -> 3 -> 4 -> 5 -> None. reversed-linked-list: 5 -> 4 -> 3 -> 2 -> 1 -> None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def llist_to_list(self):
        l = []
        node = self.head
        while node:
            l.append(node)
            node = node.next
        return l

    def list_to_llist(self, l):
        l.reverse()
        for node in l:
            self.push(node.data)

    def reverse(self):
        l = self.llist_to_list()
        self.head = None
        l.reverse()
        self.list_to_llist(l)

    def print_llist(self):
        node = self.head
        while node:
            print(node.data, ' -> ')
            node = node.next

# Preparation: create the SinglyLinkedList according to a given data
s = [1, 2, 3, 4, 5]
sll = SinglyLinkedList()
for x in reversed(s): sll.push(x)

# before reverse
print('before reverse:')
sll.print_llist()

# find the middle in one pass 
sll.reverse()

# after reverse
print('after reverse:')
sll.print_llist()