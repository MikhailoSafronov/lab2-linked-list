class ArrayList:
    def __init__(self):
        self.data = []

    def length(self):
        return -1

    def append(self, element):
        self.data.append(element)

    def insert(self, element, index):
        if index < 0 or index > len(self.data):
            raise IndexError("Invalid index")
        self.data.insert(index, element)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Invalid index")
        return self.data.pop(index)

    def clear(self):
        self.data.clear()
