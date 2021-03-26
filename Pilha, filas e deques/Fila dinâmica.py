class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.length = 0
        self.first = None
        self.last = None

    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
            self.length +=1
        else:
            new_node.next = self.last
            self.last = new_node
            self.length +=1

    def dequeue(self):
        if self.is_empty():
            print('Is empty')
        else:
            current_node = self.last
            while current_node.next != self.first:
                current_node = current_node.next
            self.first = current_node
            current_node.next = None
        self.length -=1

    def display(self):
        if self.is_empty():
            print('Is empty')
        else:
            current_node = self.last
            while current_node:
                print(current_node.value, end = ' ')
                current_node = current_node.next
        print()

    def search_by_value(self, value):
        if self.is_empty():
            print('Is empty')
            return False
        else:
            current_node = self.last
            while current_node:
                if current_node.value == value:
                    return True
                current_node = current_node.next
            return False

    def size(self):
        return self.length

queue = Queue()
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(9)
queue.enqueue(10)
queue.enqueue(23)
queue.enqueue(1)
queue.enqueue(2)
queue.display()
queue.dequeue()
queue.display()
print(queue.size())
print(queue.search_by_value(8))
