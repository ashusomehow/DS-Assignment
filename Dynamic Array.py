class DynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.resize_factor = resize_factor

# Inserts an element at the specified index.
    def insert_at_index(self, index, value):
        if index < 0 or index > len(self.array):
            raise IndexError("Index out of bounds")
        self.array.insert(index, value)

#Deletes the element at the specified index.
    def delete_at_index(self, index):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of bounds")
        del self.array[index]

# Returns the size of the linked list.
    def get_size(self):
        return len(self.array)

# Returns true if the linked list is empty, false otherwise.
    def is_empty(self):
        return len(self.array) == 0


# Reverses the linked list.
    def reverse(self):
        self.array.reverse()

#Appends an element to the end of the linked list.
    def append(self, value):
        self.array.append(value)

#Returns the middle element of the linked list.
    def get_middle_element(self):
        if len(self.array) == 0:
            return None
        mid_index = len(self.array) // 2
        return self.array[mid_index]