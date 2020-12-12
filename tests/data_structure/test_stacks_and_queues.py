from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import (Stack, Queue)

# **************************** Stacks ********************************

def test_push():
    stack = Stack()
    stack.push(5)
    actual = stack.top.value
    expected = 5
    assert actual == expected

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    actual = stack.top.value
    expected = 2
    assert actual == expected
    
def test_peek_Stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.peek()
    actual = stack.top.value
    expected = 3
    assert actual == expected

def test_isEmpty_Stack():
    stack = Stack()
    stack.is_empty()
    actual = stack.top
    expected = None
    assert actual == expected



# **************************** Queues ********************************

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.front.value
    expected = 1
    assert actual == expected

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    actual = queue.front.value
    expected = 2
    assert actual == expected

def test_peek_Queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.peek()
    actual = queue.front.value
    expected = 1
    assert actual == expected

def test_isEmpty_Queue():
    queue = Queue()
    queue.is_empty()
    actual = queue.front
    expected = None
    assert actual == expected
