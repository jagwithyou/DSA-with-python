class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None #To track the starting point of the linked list

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def get_end_value(self):
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        return iterator

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return 
        end_node = self.get_end_value() 
        end_node.next = Node(data, None)
    
    def insert_values(self, values):
        for value in values:
            self.insert_at_end(value)
    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count +=1
            iterator = iterator.next
        return count

    def print(self):
        if self.head == None:
            print("Linked List is empty")
        iterator = self.head
        result = ""
        while iterator:
            result += str(iterator.data) + " --> "
            iterator = iterator.next
        print(result)
    def get_element_at(self, index):
        if index <=0 and index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
        counter = 0
        iterator = self.head
        while iterator:
            if counter == index:
                return iterator
            counter += 1
            iterator = iterator.next

    def remove_element_at(self, index):
        if index <=0 and index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
        counter = 0
        iterator = self.head
        while iterator:
            if counter == index-1:
                iterator.next = iterator.next.next
                break
            counter += 1
            iterator = iterator.next
        

    def insert_element_at(self, index, data):
        if index <0 and index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            node = Node(data, self.head)
            self.head = node
        counter = 0
        iterator = self.head
        while iterator:
            if counter == index-1:
                node = Node(data, iterator.next)
                iterator.next = node
                break
            counter += 1
            iterator = iterator.next
        

if __name__=="__main__":
    linked_list = LinkedList()
    linked_list.insert_at_begining(6)
    linked_list.insert_at_begining(5)
    linked_list.insert_at_end(7)
    linked_list.insert_values([8,9,10])
    linked_list.print()
    print("Length : "+ str(linked_list.get_length()))
    print(linked_list.get_element_at(2).data)
    linked_list.remove_element_at(2)
    linked_list.print()
    linked_list.insert_element_at(2, 7)
    linked_list.insert_element_at(0, 4)
    linked_list.print()