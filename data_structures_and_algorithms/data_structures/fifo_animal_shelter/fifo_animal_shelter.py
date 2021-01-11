class AnimalShelter:
    def __init__(self):
        self.storage = []
        self.type = []



    '''
    Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
    Implement the following methods:
    enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
    dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.
    '''
    
    def enqueue(self, animal, animal_type):
        if animal:
            if animal == 'cat' or animal == 'dog':
                self.storage.append(animal)
                self.type.append(animal_type)
            else:
                return('please add a cat or dog')


    def dequeue(self, pref):
        if pref:
            while len(self.type) != 0:
                if self.peek_at_type() == pref:
                    return (self.peek_at_animal(), self.peek_at_type())
                else:
                    self.storage.pop()
                    self.type.pop()

            return None
        
        else:
            return ('please enter your favorite animal')

        


    def peek_at_animal(self):
        try:
            return self.storage[0]
        except:
            return('No values were found')

    def peek_at_type(self):
        try:
            return self.type[0]
        except:
            return('No values were found')


if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue('cat','cat1')
    shelter.enqueue('dog','dog1')
    shelter.enqueue('dog','dog3')
    shelter.enqueue('cat','cat2')
    print('peeked animal: ', shelter.peek_at_animal())
    print('peeked type: ', shelter.peek_at_type())
    print(shelter.dequeue('cat1'))



# from data_structures_and_algorithms.stacks_and_queues.stacks_and_queues import Node,Queue
# class Dog:
#     type = 'dog'
#     def __init__(self,name):
#         self.name = name

# class Cat:
#     type = 'cat'
#     def __init__(self,name):
#         self.name = name

# class AnimalShelter():
#     def __init__(self):
#         self.dogs = Queue()
#         self.cats = Queue()

#     def enqueue(self,animal):
#         try:
#             if animal.type == 'cat':
#                 self.cats.enqueue(animal)
#             elif animal.type == 'dog':
#                 self.dogs.enqueue(animal)
#         except AttributeError as e:
#             return 'Add Cat or Dog Only'

#     def dequeue(self,pref):

#         try:
#             if pref == 'cat':
#                 cat = self.cats.dequeue()
#                 return cat.name
#             elif pref == 'dog':
#                 dog = self.dogs.dequeue()
#                 return dog.name
#         except AttributeError as e:
#             return None