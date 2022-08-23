class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, node): # Adding an element before the first element
        new_node = Node(node) # creating a new node with a desired value
        new_node.next = self.head # newly created node's new pointer will refer to the old head
        if self.head:
            self.head.prev= new_node # old head's prev pointer will refer to the newly created node
            self.head = new_node # new node becomes the new head
            new_node.prev = None
        else: # if the list is empty make the new node both head and tail
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

    def push_back(self, node): # adding the element after the last element
        new_node = Node(node)
        new_node.prev = self.tail # connecting node to the tail
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else: # remember that we have a tail element here to which we can adjust
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    def return_first(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            return self.head.data

    def return_last(self):
        if self.tail is None:
            print("List is empty")
            return
        else:
            return self.tail.data

    def pop_front(self): # removes and returns the first element
        if self.head is None:
            print("List is empty")
            return
        else:

            first = self.head
            first.next.prev = None # remove the previous pointer that was pointing to the first
            self.head = first.next
            first.next = None # remove the next pointer of the removed first pointer
            return first.data

    def pop_back(self):
        if self.tail is None:
            print("The list is empty")
            return
        else:
            back = self.tail
            back.prev.next = None # removes the next pointer referring to the old tail
            self.tail = back.prev # make second to the last element the new tail
            back.prev = None # remove previous pointer referring to the new tail
            return back.data


    def insert_after(self, temp_node, new_data): # insert after a given node
        if temp_node is None:
            print("Given node is empty")
        else:
            new_node = Node(new_data) # created a new node to insert
            # here we don't need to traverse, unlike the single linked list!
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node

            if new_node.next != None:
                new_node.next.prev = new_node

            if temp_node == self.tail: # don't forget to check for this condition: checks if it is being added to the tail
                self.tail = new_node # then makes new node the new tail

    def insert_before(self, temp_node, new_data):
        if temp_node is None:
            print("Given node is empty")
        else:
            new_node = Node(new_data)
            new_node.prev = temp_node.prev
            temp_node.prev = new_node
            new_node.next = temp_node
            # make sure that the previos node's next is connected to the new node if it is the new node
            if new_node.prev != None:
                new_node.prev.next = new_node
            if temp_node == self.head: # check if the new node is being added before the first element
                self.head = new_node # makes new node the new head
                




















    def push_list(self, lst):
        lst = lst[::-1]
        for i in lst:
            linked_list = self.push(i)
        return linked_list

    def display(self):
        if self.head is None:
            print("This is an empty linked list.")
            return
        current = self.head
        lst = []
        while current:
            lst.append(current.data)
            current = current.next
        print(lst)


lst = doubly_linked_list()
array = [1, 2, 3]
lst.push_list(array)
lst.display()







