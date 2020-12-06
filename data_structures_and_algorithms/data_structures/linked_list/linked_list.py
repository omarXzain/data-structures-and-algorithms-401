class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

# *********************************************

    def insert(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
        
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        return node.value

# *********************************************

    def includes(self, value):
        current = self.head
        while current.next != None:
            if current.value == value:
                return True
            else:
                current = current.next
                return False

# ***********************************************

    def to_string(self):
        current = self.head
        current_string = f" { {current.value} }"

        while current.next:
            current = current.next
            current_string += f" -> { {current.value} }"

        return f"{ current_string } -> NULL"

    

if __name__ == "__main__":
    list1 = Linkedlist()
    list1.insert(15)
    list1.insert(8)
    list1.insert(6)
    list1.insert(3)

    print(list1.includes(15))
    print(list1.includes(8))

    print(list1.to_string())