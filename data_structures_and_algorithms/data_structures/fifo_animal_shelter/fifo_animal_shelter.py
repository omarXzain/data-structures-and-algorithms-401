class AnimalShelter:
    def __init__(self):
        self.storage = []
        self.type = []

    def enqueue(self, animal, animal_type):
        if animal:
            if animal == 'cat' or animal == 'dog':
                self.storage.append(animal)
                self.type.append(animal_type)
            else:
                return('please add a cat or dog')


    def dequeue(self, pref):
        # print(pref)
        # print(self.type, self.storage)
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
