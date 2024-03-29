class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create and Handle list operations
class LinkedList:
    def __init__(self):
        self.head = None  # Head of list

    # 1. Method to reverse the list iteratively
    def reverse_iteratively(self):

        previous = None
        current = self.head
        while current:
            temporary = current.next
            current.next = previous
            previous = current
            current = temporary

        self.head = previous


    # 2. Method to reverse the list recursively
    def reverse(self, head):
        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head
        # Reverse the rest list
        rest = self.reverse(head.next)
        # Put first element at the end
        head.next.next = head
        head.next = None
        # Fix the header pointer
        return rest

    # 3. Pushes new data to the head of the list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    #4.a Append data to the end of the list
    def append(self, data):

        if self.head is None:
            self.head = Node(data)
            return

        new_node = Node(data)
        current = self.head
        #traverse the list
        while current.next:
            current = current.next
        current.next = new_node

    # 4.b. Convert an array to a linked list, same as append but put in a loop 
    def arrayToList(self, arr):
        
        for i in range(len(arr)):
            if self.head is None:
                self.head = Node(arr[i])

            new_node = Node(arr[i])
            current = self.head
            # traverse the list
            while current.next:
                current = current.next
            current.next = new_node

    #5.  display data
    def display(self):
        if self.head is None:
            print("The linked list is empty")
            return

        temp = self.head
        elems = []
        while temp != None:
            elems.append(temp.data)
            temp = temp.next
        print(elems)

    # 6. Find the length of a linked list

    def length(self):

        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter


    # 7. Insert data at an index

    def insert_at(self, index, data):

        if index >= self.length() or index < 0:
            raise Exception("Invalid Index")

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            # always adjust a new head
            self.head = new_node
            return

        current = self.head
        indx = 0
        while current:

            if indx == index-1:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                break
            #to keep iterating
            current = current.next
            indx += 1

    # 8. Insert data after an index

    def insert_after(self, index, data):

        if index >= self.length() or index < 0:
            raise Exception("Invalid Index")

        new_node = Node(data)
        current = self.head
        indx = 0

        while current:
            if indx == index:
                #tying together to prevent the break of links
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            indx += 1

    # 9. Insert data after a value

    def insert_after_value(self, value, data):

        if self.head is None:
            return

        new_node = Node(data)
        current = self.head

        while current:
            if value == current.data:
                # tying the nodes
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    # 9a. Insert a node in a sorted list:

    def insert_in_sorted(self, data):

        new_node = Node(data)
        current = self.head

        # if head is None or head.data is less than a new node data

        if current is None or current.data < new_node.data:
            new_node.next = current
            current = new_node
            return

        # traverse the list but stop at current next in order to catch
        # the correct current that would be previos
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node


    # 10. remove data by index

    def remove_by_index(self, index):

        if index >= self.length() or index < 0:
            raise Exception("Invalid Index")

        if index == 0:
            # setting head to the next element after self.head
            self.head = self.head.next
        indx = 0
        current = self.head
        previous = None

        while current.next != None:
            previous = current
            current = current.next

            if indx == index-1:
                previous.next = current.next
                pass
            indx +=1

    # 11. Remove data by value

    def remove_by_value(self, value):

        if self.head is None:
            return
        # setting head to the next element after self.head
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current:

            if current.data == value:
                previous.next = current.next
                return

            previous = current
            current = current.next
    
    # 12 Merge two sorted lists through the recursion

        def mergeTwoLists(self, list1, list2):
            # creating an empty node that is stable at the beginning 
            dummy = Node()
            # creating a node for traversal 
            current = dummy 
            
            while list1 and list2: 
                
                if list1.data < list2.data:
                    current.next = list1
                    list1 = list1.next 
                else:
                    current.next = list2
                    list2 = list2.next 
                    
                current = current.next
            
            # Make sure to atach remaining elements if one of the lists is still not empty
            if list1: 
                current.next = list1
            elif list2:
                current.next = list2
                
            return dummy.next


# 13 Merge two sorted lists. Recursion 

# Function to merge two sorted linked list.
def mergeLists(head1, head2):

    # List1 is empty then return List2
    if head1 is None:
        return head2

    # if List2 is empty then return List1
    if head2 is None:
        return head1

    # If List1's data is smaller or
    # equal to List2's data
    if head1.data <= head2.data:

        # Again check List1's data is smaller or equal List2's
        # data and call mergeLists function.
        head1.next = mergeLists(head1.next, head2)
        return head1
        
    else:
  
        # Again check List2's data is greater or equal List's
        # data and call mergeLists function.
        head2.next = mergeLists(head1, head2.next)
        return head2

# 14. Insert in a sorted list using dummy:

def insert_in_sorted_using_dummy(head, data):
    dummy = LinkedList()
    current = dummy
    new_node = Node(data)

    # Assigning a head to the dummy
    dummy.next = head

    while current.next and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return dummy.next










# Driver code
L = LinkedList()
L.push(1)
L.push(2)
L.push(3)
L.push(4)
L.head = insert_in_sorted_using_dummy(L.head, 4)
L.display()
L.insert_in_sorted(4)
L.display()

L.push("apple")
L.display()
#L.insert_after_value("apple", 102)
L.remove_by_index(0)
L.remove_by_value("apple")
L.display()


print("Given linked list")


#L.head = L.reverse(L.head)

#L.reverse_iteratively()

# L.insert_after(0, 101)
#
# L.display()
#
# print("Reversed linked list")
# print(L)