
class Node:


    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:


    def __init__(self):
        self.head = None


    def is_empy(self):
        if (self.head == None):
            return True
        return False

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linkedList = LinkedList()

print(linkedList.is_empy())

linkedList.insert(2)

print(linkedList.is_empy())

linkedList.insert(3)

linkedList.insert(4)

linkedList.display_forward()


