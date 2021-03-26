class Queue:
    def __init__(self):
        self.items = []

    def append(self, value):
        self.items.insert(0, value)

    def pop(self):
        self.items.pop()

    def display(self):
        print(self.items)

    def search_by_value(self, value):
        for i in self.items:
            if i == value:
                return True
        return False

queue = Queue()
queue.append(1)
queue.append(4)
queue.append(2)
queue.append(6)
queue.append(8)
queue.append(10)
queue.append(3)
queue.display()
queue.pop()
queue.display()
print(queue.search_by_value(4))
print(queue.search_by_value(5))