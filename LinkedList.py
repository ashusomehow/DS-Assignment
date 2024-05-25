class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.size = 0
# Inserts an element at the specified index.
    def insert_at_index(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

# Deletes the element at the specified index.
    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

# Returns the size of the dynamic array.
    def get_size(self):
        return self.size

# Returns true if the dynamic array is empty, false otherwise.
    def is_empty(self):
        return self.size == 0

# Reverses the dynamic array.
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Appends an element to the end of the dynamic array.
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

# Merges two dynamic arrays into a single dynamic array.
    def merge(self, other):
        if self.head is None:
            self.head = other.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other.head
        self.size += other.size
        other.head = None
        other.size = 0

# Interleaves two dynamic arrays into a single dynamic array.
    def interleave(self, other):
        dummy = Node()
        tail = dummy
        l1, l2 = self.head, other.head
        while l1 and l2:
            tail.next, l1 = l1, l1.next
            tail = tail.next
            tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        self.head = dummy.next
        self.size += other.size
        other.head = None
        other.size = 0





