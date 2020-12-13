from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
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


