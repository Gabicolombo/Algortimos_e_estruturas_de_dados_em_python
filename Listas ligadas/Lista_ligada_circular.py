class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # First element
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
            return

        new_node = Node(data)
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next

        current_node.next = new_node
        new_node.next = self.head
        return

    def display(self):
        current_node = self.head

        while current_node:
            print(f'{current_node.data}', end=' ')
            current_node = current_node.next
            if current_node == self.head:
                break

        print('\n-----------')
        return

    def insert_by_index(self, index, data):
        if index <0 or index >= self.length():
            print('Error')
            return

        current_node = self.head
        new_node = Node(data)
        previous_node = None
        if self.head == None:
            self.head.next = new_node
            return
        elif index == 0:
            new_node.next = current_node.next
            self.head.next= new_node
            return
        else:
            idx = 0
            while idx < index:
                previous_node = current_node
                current_node = current_node.next
                idx +=1


        previous_node.next = new_node
        new_node.next = current_node

        return

    def length(self):
        if self.head == None:
            return 0

        total = 0
        current_node = self.head

        while current_node:
            current_node = current_node.next
            total +=1
            if current_node == self.head:
                break

        return total

    def remove(self):
        if self.head == None:
            print('Error')
            return

        current_node = self.head

        while current_node:
            current_node = current_node.next
            if current_node.next.next == self.head:
                break


        current_node.next = self.head
        return

    def remove_by_index(self, index):
        if index < 0 or index >= self.length():
            print('Error')
            return

        if self.head == None:
            print('Error')
            return

        if index == 0:
            current = self.head

            while current:
                current = current.next
                if current.next == self.head:
                    break

            current.next = self.head.next
            self.head = self.head.next
        else:
            current_node = self.head
            previous_node = None
            idx = 0

            while idx <= index - 1:
                previous_node = current_node
                current_node = current_node.next
                idx += 1

            previous_node.next = current_node.next

        return

    def get(self, index):
        if index < 0 or index >= self.length():
            print('Error')
            return

        current_node = self.head
        idx = 0
        if index == 0:
            return self.head.data
        while idx < index:
            current_node = current_node.next
            idx +=1
        return current_node.data


    def search_by_item(self, item):
        if self.head == None:
            print('Error')
            return

        current_node = self.head
        data = None
        while current_node:
            if current_node.data == item:
                data = current_node.data
                break
            if current_node.next == self.head:
                break
            current_node = current_node.next

        if data != None:
            return data
        else:
            return "Error: we don't have it"

    def to_list(self):
        if self.head == None:
            print('Error')
            return

        data = []
        current_node = self.head

        while current_node:
            data.append(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break


        print(f'List: {data}')




my_list = CircleLinkedList()
my_list.append(2)
my_list.append(6)
my_list.append(10)
my_list.append(8)
my_list.display()
my_list.to_list()
print(my_list.length())
my_list.insert_by_index(3, 13)
my_list.display()
my_list.remove()
my_list.display()
my_list.remove_by_index(3)
my_list.display()
print(my_list.get(0))
print(my_list.search_by_item(10))