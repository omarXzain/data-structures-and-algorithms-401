class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

# *********************************************

    '''
    problem domain
    Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance
    
    Algorithm
    1. Create function called insert takes a value
    2. create a variable and put the value inside it
    3. if head exist make the next node equal to none
    4. make head equal to the next node
    5. return node
    
    Big(o) >>>>
    
    Time O(1)
    Space O(1)
    
    '''


    def insert(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
        
        else:
            node.next = self.head
            self.head = node
        return node.value

# **********************************************
    '''
    Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    
    1. Create function called include that takes a value.
    2. check if the head is none then return a false
    3. else make current variable and put the head inside it 
    4. if the next current equal to value return a true 
    
    
    def include(self, value):
        if self.head == None:
            return False
        else:
            current = self.head 
            if current.value == value:
                return True
            else:
                current = current.next
            return false

    '''
    
    
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

    '''
    Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
    "{ a } -> { b } -> { c } -> NULL"
    
    
    1. create a functiom called toString
    2. create a variable and put the head inside it
    3. if the head not equal to none then return a string
    
    def __str__(self):
        current = self.head
        stg = ""
        while current.next:
            stg += 

    
    '''
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
    '''
    .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
    algorithm:
    1. create function callled insert_before that tkes two para the fisrt one is value i want to add before and the value to added 
    2. check if the head is null then will make the head equal to the node
    3 assign cureent equal to head
    4. keep moving until (cuerrnt.next) reaches the value(check if the current.next.value equal to value )    
    5. new=Node(newValue)

    
    
    '''
    def insertBefore(self, x, newVal):
        node = Node(newVal)
        if self.head is None:
            self.head = node

        else:
            current = self.head

            if current.value == x:
                node.next = self.head
                self.head = node

            else :
                while current.next.value != x:
                    current = current.next

                if current.next.value == x:
                    old = current.next
                    current.next = node
                    node.next = old

    # def insertBefore(self,val,newValue):   
    #     node=Node(newValue)
    #     if self.head==None:
    #         self.head=node
    #     else:
    #         cur=self.head
    #         while(cur.value==val):
    #             cur.next=node
    #             node.next=cur.next
    #         cur=cur.next


    # def insertBefore(self,value,newVal):
    #     node = Node(newVal)
    #     if self.head.value == value:
    #         return(self.insert(newVal))
    #     current = self.head
    #     while current.next.value != value:
    #         current = current.next
    #     node.next = current.next
    #     current.next = node  
# ***********************************************

    def insertAfter(self, x, newVal):
        node = Node(newVal)
        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.value != x:
                current = current.next

            if current.value == x:
                old = current.next
                current.next = node
                node.next = old

# ***********************************************

# Write a method for the Linked List class which takes a number,
# k, as a parameter. Return the node’s value that is k from the end of the linked list. 
    
    def ll_kth_from_end(self, k):
        
        current = self.head
        length = 0
        pos = 0

        while current:
            length +=1
            current = current.next
            
        pos = length - k - 1

        if (pos < 0 or k < 0):
            return f'Exception'

        current = self.head
        while pos:
            current = current.next
            pos = pos -1
        
        return current.value

# *************************************************

    ## Fixed
    def zip_lists(self, list2):
        ll = Linkedlist()
        current1 = self.head
        current2 = list2.head

        while current1 and current2:
            ll.append(current1.value)
            ll.append(current2.value)
            current1 = current1.next
            current2 = current2.next
        return ll


# *************************************************'

if __name__ == "__main__":
    
    list1 = Linkedlist()
    list2 = Linkedlist()
    # print('************ insert **********')
    # list1.insert(9)
    # list1.insert(7)
    # list1.insert(3)
    # list1.insert(1)
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)
    list1.insert(5)
    list1.insert(6)
    # print(' *********** includes ***********')
    # print(list1.includes(2))
    # print(list1.includes(8))
    # print(list1.includes(3))
    # print(list1.includes(1))
    # print(list1.includes(12))
    # print(list1.includes(0))
    # print(' *********** to string ***********')
    print(list1.to_string())
    print(' ********** kth from end************')
    print(list1.ll_kth_from_end(0))
    # print(list1.ll_kth_from_end(2))
    # print(list1.ll_kth_from_end(6))
    # print('*********** append ***********')
    # list1.append(1)
    # list1.append(2)
    # list1.append(3)
    # list2.append(9)
    # list2.append(10)
    # list2.append(11)
    # print('*********** zipped List ***********')
    print('l1: ', list1.to_string())
    print('l2: ', list2.to_string())
    print('final: ', list1.zip_lists(list2).to_string())
    # print('*********** insert before ***********')
    list1.insertBefore(3, 5)
    list1.insertBefore(1, 0)
    # print('***********insert after ***********')
    list1.insertAfter (3,-1000)
    print(' *********** to string ***********')
    print(list1.to_string())

