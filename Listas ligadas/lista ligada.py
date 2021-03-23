class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):

        new_none = Node(data)

        # se tiver vazia
        if self.head == None:
            self.head = new_none
            return

        current_none = self.head

        # vai navegar pela lista encadeada
        # vai parar quando chegar no None
        while current_none.next:
            current_none = current_none.next

        # colocamos o new_none no ultimo lugar
        current_none.next = new_none
        return


    def length(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0

        while current_node:
            total += 1
            current_node = current_node.next
        return total

    # convertendo para um array normal
    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next

        return node_data

    # printar
    def display(self):
        contents = self.head

        if contents is None:
            print('List has no element')

        while contents:
            print(contents.data, end = ' ')
            contents = contents.next

        print("\n----------")


    def get(self, index):
        if index >= self.length() or index < 0:
            return 'Error: Index out of range'

        current_idx = 0
        current_node = self.head

        while current_node != None:
            if current_idx == index:
                return current_node.data

            current_node = current_node.next
            current_idx += 1

    # reverter a lista encadeada
    def reverse_linkedlist(self):
        if self.head == None:
            return 'Error'
        previous_node = None
        current_node = self.head

        while current_node != None:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next

        self.head = previous_node

    def search_item(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                return True

            current_node = current_node.next

        return False

    def remove_at_start(self):
        if self.head == None:
            return 'The list is empty'

        current_node = self.head
        self.head = current_node.next
        return 'Ok'


    def remove_at_end(self):
        if self.head == None:
            return 'Sorry, this list is empty'

        current_node = self.head
        previous_node = ''
        index = self.length()
        count = 0
        while count < index - 1:
            previous_node = current_node
            current_node = current_node.next
            count+=1

        previous_node.next = None
        return 'Ok'

    def insert_at_start(self, data):
        new_node = Node(data)

        aux = self.head
        new_node.next = aux
        self.head = new_node

        return 'OK'



    def insert_at_end(self, data):
        if self.head == None:
            return 'Error: this list is empty'

        new_node = Node(data)
        current_node = self.head

        while current_node:
            if current_node.next == None:
                break
            current_node = current_node.next


        current_node.next = new_node
        return 'OK'

    def remove_element_by_value(self, data):
        if self.search_item(data):
            current_node = self.head
            previous_node = ''
            while current_node:
                if current_node.data == data:
                    previous_node.next = current_node.next
                previous_node = current_node
                current_node = current_node.next
            return 'Ok'
        return False

    def insert_at_index(self, index, data):
        if index >= self.length() or index < 0:
            return False

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return 'Ok'

        if index == 0:
            self.insert_at_start(data)
            return 'Ok'

        if index == self.length()-1:
            self.insert_at_end()
            return 'OK'

        idx = 1
        current_node = self.head
        previous_node = ''

        while idx <= index:
            previous_node = current_node
            current_node = current_node.next
            idx += 1

        previous_node.next = new_node
        new_node.next = current_node

        return 'OK'


# Test
my_list = LinkedList()
my_list.display()

my_list.append(3)
my_list.append(7)
my_list.append(2)
my_list.append(1)

my_list.display()

print(f"The total number of elements are: {my_list.length()}")
print(my_list.to_list())

print('---------')
my_list.reverse_linkedlist()
my_list.display()

print(my_list.get(2))
print(my_list.search_item(3))
print(my_list.search_item(8))

print(my_list.remove_at_start())
my_list.display()

print(my_list.remove_at_end())
my_list.display()

print(my_list.insert_at_start(10))
my_list.display()

print(my_list.insert_at_end(9))
my_list.display()

print(my_list.remove_element_by_value(2))
my_list.display()

print(my_list.insert_at_index(0, 15))
print(my_list.insert_at_index(2, 8))
my_list.display()