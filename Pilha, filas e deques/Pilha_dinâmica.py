class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.__total = 0

    def push(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.__total +=1

    def length(self):
        return self.__total

    def is_empty(self):
        if self.__total == 0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            print('Empty')
            return

        self.head = self.head.next
        self.__total -=1

    def display(self):
        if self.is_empty():
            print('Empty')
            return

        nav = self.head
        while nav:
            print(nav.data, end=' ')
            nav = nav.next

        print('\n----------')

    def search_an_item(self, data):
        if self.is_empty():
            return 'Empty'
        nav = self.head
        while nav:
            if nav.data == data:
                return nav.data
            nav = nav.next
        return 'Error: this value does not exist'

stack = Stack()
stack.push(10)
stack.push(56)
stack.push(1)
stack.push(3)
stack.push(7)
stack.push(0)
stack.display()
print(f'Is empty? {stack.is_empty()}')
print(f'Length: {stack.length()}')
print(stack.search_an_item(134))
stack.pop()
stack.pop()
stack.display()