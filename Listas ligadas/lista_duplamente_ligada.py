class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoubleNode(data)

        new_node.next = None

        if self.head == None:
            new_node.previous = None
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

        new_node.previous = last_node
        return

    def length(self):
        if self.head == None:
            return 0

        current_node = self.head
        total = 0
        while current_node:
            current_node = current_node.next
            total +=1

        return total

    def insert_at_start(self, data):
        new_node = DoubleNode(data)
        if self.head == None:
            self.head = new_node
            return

        current_node = self.head
        new_node.next = current_node
        self.head = new_node
        current_node.previous = new_node

        return

    def insert_at_end(self, data):
        new_node = DoubleNode(data)
        if self.head == None:
            self.head = new_node

        current_node = self.head
        last_node = ''

        while current_node:
            if current_node.next == None:
                last_node = current_node
            current_node = current_node.next

        last_node.next = new_node
        return

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.length():
            return 'Error'

        new_data = DoubleNode(data)

        if self.head == None:
            self.head = new_data
            return

        if index == 0:
            self.insert_at_start(data)
            return

        if index == self.length() -1:
            self.insert_at_end(data)
            return

        current_node = self.head
        idx = 0
        previous_node = ''
        next_node = ''
        while current_node:
            if idx == index:
                previous_node = current_node.previous
                next_node = current_node
                break
            current_node = current_node.next
            idx +=1


        previous_node.next = new_data
        new_data.previous = previous_node
        next_node.previous = new_data
        new_data.next = next_node
        return


    def display(self):
        if self.head == None:
            print('Error')

        current_node = self.head

        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next


        print('\n--------------------')

    def to_list(self):
        if self.head == None:
            print('Error')
            return False

        data_list = []
        current_node = self.head

        while current_node:
            data_list.append(current_node.data)
            current_node = current_node.next

        print(data_list)
        return

    def get(self, index):
        if self.head == None:
            return 'Error'

        current_node = self.head
        idx = 0

        while current_node:
            if idx == index:
                return current_node.data
            idx += 1
            current_node = current_node.next

        return 'Error'

    def search_item(self, data):
        if self.head == None:
           return False

        current_node = self.head


        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next

        return False

    def reverse_doublelinkedlist(self):
        if self.head == None:
            print('Error')
            return

        previous_node = None
        current_node = self.head

        while current_node != None:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next

        self.head = previous_node

        return

    def remove_at_start(self):
        if self.head == None:
            return 'Error'

        current_node = self.head

        self.head = current_node.next
        return

    def remove_at_end(self):
        if self.head == None:
            return 'Error'

        current_node = self.head
        previous_node = ''
        index = self.length()
        idx = 0
        while idx < index -1:
            previous_node = current_node
            current_node = current_node.next

            idx +=1

        previous_node.next = None
        current_node.previous = None
        return


    def remove_element_by_value(self, value):
        if self.search_item(value) == False:
            return False

        current_node = self.head
        while current_node:
            if current_node.data == value:
                break
            current_node = current_node.next

        previous_node = current_node.previous
        next_node = current_node.next

        previous_node.next = next_node
        next_node.previous = previous_node

        return True


# Test
my_list = DoubleLinkedList()
my_list.append(10)
my_list.append(13)
my_list.append(40)
print(f'The total number of elements are: {my_list.length()}')
my_list.display()
my_list.insert_at_start(9)
my_list.display()
my_list.insert_at_end(2)
my_list.display()
my_list.insert_at_index(2, 15)
my_list.display()
print(my_list.search_item(15))
print(my_list.get(5))
my_list.remove_at_start()
my_list.display()
my_list.remove_at_end()
my_list.display()
print(my_list.remove_element_by_value(13))
my_list.display()
my_list.to_list()
my_list.reverse_doublelinkedlist()
my_list.display()