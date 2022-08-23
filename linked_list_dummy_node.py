class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def at_at_head(self, data):
        self.add_at_index(0, data)

    def append(self, data):
        self.add_at_index(self.size, data)

    def array_to_ll(self, arr):
        for i in range(len(arr)):
            ll = self.add_at_index(self.size, arr[i])
        return ll

    def display(self):

        elems = []
        current = self.head.next
        while current:
            elems.append(current.data)
            current = current.next

        print(elems)

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index+1):
            current = current.next

        return current.data

    def add_at_index(self,index, data):
        if index > self.size:
            return

        if index < 0:
            index = 0

        self.size += 1

        new_node = Node(data)
        current = self.head
        for _ in range(index):
            current = current.next

        new_node.next = current.next
        current.next = new_node


    def delete_at_index(self, index):

        if index < 0 or index >= self.size:
            return

        current = self.head
        for _ in range(index):
            current = current.next

        current.next = current.next.next


    def remove_elements(self, data):

        new_node = Node(data)
        current = self.head
        while current.next:
            if current.next.data == new_node.data:
                current.next = current.next.next
            else:
                current = current.next
        return current.next


    def make_cycle(self, index):

        current = self.head

        for _ in range(index):
            current = current.next

        joint = current

        while current.next:
            current = current.next

        current.next = joint


    def has_cycle(self):

        fast = self.head.next
        slow = self.head

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            fast = fast.next.next
            slow = slow.next

        return True


    def detect_cycle(self):

        visited = set()

        current = self.head
        while current:
            if current in visited:
                return current
            else:
                visited.add(current)
                current = current.next
        return None

















L = LinkedList()
arr = [1, 2, 3, 4, 5]

L.array_to_ll(arr)
L.display()
L.make_cycle(4)
print(L.has_cycle())
print(L.detect_cycle())



# L.append(3)
# L.append(4)
# L.append(5)
# L.display()
#
#
# L.add_at_index(6, 0)
# L.display()
# L.delete_at_index(6)
# L.display()
# L.remove_elements(7)
# L.display()
# print(L.has_cycle())


