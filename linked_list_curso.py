from os import remove


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node


    def remove_from_front(self) -> int:
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value
    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.prev = None
        else:
            self.head = None
        return removed_value