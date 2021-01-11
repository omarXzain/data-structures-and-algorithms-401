from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
        
        ## enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
        ## dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
        '''
        1. use the stack push method to attach the value into the new stack and return it
        
        2. use the stack pop method to remove the last value from the new stock and return it         
        '''

        
class PseudoQueue():
    def __init__(self):
        self.front = Stack()
        self.back = Stack()

    def enqueue(self, value):
        return self.front.push(value)

    def dequeue(self):
        return self.front.pop()


    
if __name__ == "__main__":
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.enqueue(4)
    print('peeked: ', pseudo.front.top.value)
    print('value popped: ', pseudo.dequeue())


