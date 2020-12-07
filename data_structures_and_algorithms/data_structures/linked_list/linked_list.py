class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

# *********************************************

    def insert(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
        
        else:
            node.next = self.head
            self.head = node
        return node.value

# **********************************************

    def includes(self, value):
        current = self.head
        while current.next:
            if current.value == value:
                return True

            current = current.next
            if current.value == value:
                return True
            
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

# ***********************************************
    
    def ll_kth_from_end(self, k):
        current = self.head
        length = 0
        pos = 0

        while current:
            length = length +1
            current = current.next
            
        pos = length - k - 1

        if (pos < 0 or k < 0):
            return f'Exception'

        current = self.head
        while pos:
            current = current.next
            pos = pos -1
        
        return current.value



if __name__ == "__main__":
    list1 = Linkedlist()
    # print('************ insert **********')
    list1.insert(2)
    list1.insert(8)
    list1.insert(3)
    list1.insert(1)
    print(' *********** includes ***********')
    print(list1.includes(2))
    print(list1.includes(8))
    print(list1.includes(3))
    print(list1.includes(1))
    print(list1.includes(12))
    print(list1.includes(0))
    print(' *********** to string ***********')
    print(list1.to_string())
    print(' ********** kth from end************')
    print(list1.ll_kth_from_end(0))
    print(list1.ll_kth_from_end(2))
    print(list1.ll_kth_from_end(6))
    # print('*********** append ***********')
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    list1.append(6)
    list1.append(7)
    # print('*********** insert before ***********')
    list1.insertBefore(555, 6)
    # print('***********insert after ***********')
    list1.insertAfter(555, 6)
    print(' *********** to string ***********')
    print(list1.to_string())
    print(' **********************')

