class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        
        # Define a method called push which takes any value as an argument and adds a new node with that 
        # value to the top of the stack with an O(1) Time performance.
        '''
        1. create a new node and store it in a variable
        2. if the top node existed then set the next node to equal the top node.
        3. else set the top node to equal the new node.
        
        big O:  O(1)
        
        input: number
        output: number
        

        '''
    def push(self, data): 
        node = Node(data)
        if self.top:
            node.next = self.top
        else:
            self.top = node
        
    


# Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
# Should raise exception when called on empty stack

        '''
        1. create a variable and set it equal to the top node
        2. set the top node equal to the next node
        3. set the next node equal to none
        4. return the value of the variable of the top node
        5. else return an empty exception 
        
        big (o)
        O(1)
        '''
    
    def pop(self):
        try:
            current = self.top
            self.top = self.top.next
            self.top.next = None
            return current.value
        except:
            return('no value to pop')


# Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
# Should raise exception when called on empty stack

    '''
    return the value top node 
    return an empty exception 
    
    O(1)
    '''
    
    def peek(self):
        try:
            return self.top.value
        except:
            return('no value to peek at')

# Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.

        '''
        create isEmpty method 
        return the value node is empty or not
        
        big(o)
        o(1)
        '''
        
    def is_empty(self):
        if not self.top:
            return True
        else:
            return False

# ****************************************************************
# Create a Queue class that has a front property. It creates an empty Queue when instantiated.
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
    
    '''
    1. create enqueue method with a value inside it
    2. create a varible that store the new node and set it to the rear 
    '''

    def enqueue(self, data):
        node = Node(data)
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    # Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.Should raise exception when called on empty queue
    '''
    1. if the front value exist then set a variable and put the front node inside it
    2. set a variable with the next node of the front
    3. make the front variable equal to the next node
    4. return the value of the current front node      
    '''
            

    def dequeue(self):
        if self.front:
            current = self.front
            current2 = current.next
            self.front = current2
            return current.value
        else:
            return('Queue is Empty')

    # Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue, Should raise exception when called on empty queue


    def peek(self):
        try:
            return self.front.value
        except:
            return 'Queue is empty'

    # Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.

    def is_empty(self):
        if not self.front:
            return True
        else:
            return False




if __name__ == "__main__":
    print('*************************** Stacks ******************************')
    stack = Stack()
    print(stack.is_empty())
    stack.push(5)
    stack.push(6)
    stack.push('cat')
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())

    print('*************************** Queues ******************************')
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.peek())
    queue.dequeue()
    print(queue.peek())
    print(queue.is_empty())