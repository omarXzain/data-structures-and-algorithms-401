## Class 10: Stack and a Queue
- Stack is a linear data structure which follows a particular order in which the operations are performed. Each Node references the next Node in the stack, but does not reference its previous.

- A queue is an ordered collection of items where the addition of new items happens at one end, called the rear

### Challenge
- Write queue and stack classes with their methods

## Approach & Efficiency
- Create a Stack class contains:
1) Define a method called push big O(1)
2) Define a method called pop big O(1)
3) Define a method called peek big O(1)

- Create a Stack class contains:
- push that append new node to the end by reseting the top value
pop that remove the top from the stack and return the value and set the top vale to the top.next
peek that returns the top value without removing it

- Create a Queue class:
1) Define a method called enqueue big O(1)
2) Define a method called dequeue big O(1)
3) Define a method called peek big O(1)

- Create a Queue class:
- enqueue append new node to the end by using the rear and set the next value to it then set the rear
dequeue removes the front value returns itand set the front to the next of it
peek return the value of the front