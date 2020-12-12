class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        # return some data
        try:
            item = self.top
            self.top = self.top.next
            self.top.next = None
            return item.value
        except:
            return('no value to pop')

    def peek(self):
        try:
            return self.top.value
        except:
            return('no value to peek at')

    def is_empty(self):
        if not self.top:
            return True
        else:
            return False

# ****************************************************************

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node


    def dequeue(self):
        # return some data
        if self.front:
           current = self.front
           current2 = current.next
           self.front = current2
           return current.value
        else:
            return('Queue is Empty')


    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'Queue is empty'

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