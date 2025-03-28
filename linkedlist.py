class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        if not self.head:
            return 0
        current = self.head
        count = 1
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert(self, element, index):
        if index < 0 or index > self.length():
            raise IndexError("Invalid index")
        new_node = Node(element)
        if index == 0:
            if not self.head:
                self.head = new_node
                self.head.next = self.head
            else:
                new_node.next = self.head
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = new_node
                last.next = self.head
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Invalid index")
        current = self.head
        if index == 0:
            deleted_data = current.data
            if self.head.next == self.head:
                self.head = None
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = self.head.next
                last.next = self.head
            return deleted_data
        for _ in range(index - 1):
            current = current.next
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def clear(self):
        self.head = None
