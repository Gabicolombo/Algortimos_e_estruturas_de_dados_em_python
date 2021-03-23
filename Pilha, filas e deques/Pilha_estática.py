'''
push - adds an item to the top
pop  - removes an item from the top
'''

class Stack:
    def __init__(self):
        self.top = 0
        self.__items = []

    def push(self, item):
        self.__items.append(item)
        self.top = item

    def size(self):
        return len(self.__items)

    def pop(self):
        if self.size() == 0:
            return None
        return self.__items.pop()

    def display(self):
        if self.size() == 0:
            print('Empty')
            return
        print(self.__items)

    def search_an_item(self, value):
        if self.size() == 0:
            print('Empty')
            return

        for i in range(self.size()):
            if self.__items[i] == value:
                return True

        return False

myStack = Stack()
myStack.push(1)
myStack.push(20)
myStack.push(4)
myStack.push(6)

myStack.display()
myStack.pop()
myStack.display()
print(myStack.search_an_item(4))
