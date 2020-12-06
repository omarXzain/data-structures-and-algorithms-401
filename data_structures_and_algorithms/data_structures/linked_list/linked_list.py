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

# ***********************************************

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

# ***********************************************

    def insertBefore(self, value, newVal):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode

        else:
            current=self.head

            if current.value == newVal:
                newNode.next = self.head
                self.head = newNode

            else :
                while current.next.value != newVal:
                    current = current.next

                if current.next.value == newVal:
                    old = current.next
                    current.next = newNode
                    newNode.next = old
    
# ***********************************************
    
    def insertAfter(self, value, newVal):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            current=self.head

            while current.value != newVal:
                current = current.next

            if current.value == newVal:
                old = current.next
                current.next = newNode
                newNode.next = old

    


    

if __name__ == "__main__":
    list1 = Linkedlist()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    list1.insert(15)
    list1.insert(8)
    list1.insert(6)
    list1.insert(3)
    list1.includes(15)
    list1.includes(8)
    # list1.insertBefore(555, 6)
    # list1.insertAfter(555, 6)
    print(list1.to_string())