from data_structures_and_algorithms.data_structures.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter


def test_enqueue():
    shelter = AnimalShelter()
    shelter.enqueue('cat','cat1')
    actual = shelter.peek_at_type()
    expected = 'cat1'
    assert actual == expected

def test_enqueue2():
    shelter = AnimalShelter()
    shelter.enqueue('dog','dog1')
    actual = shelter.peek_at_animal()
    expected = 'dog'
    assert actual == expected

def test_enqueue3():
    shelter = AnimalShelter()
    actual = shelter.peek_at_animal()
    expected = 'No values were found'
    assert actual == expected

def test_enqueue4():
    shelter = AnimalShelter()
    actual = shelter.peek_at_type()
    expected = 'No values were found'
    assert actual == expected


def test_dequeue():
    shelter = AnimalShelter()
    shelter.enqueue('cat','cat1')
    shelter.enqueue('dog','dog1')
    shelter.enqueue('dog','dog3')
    actual = shelter.dequeue('cat1')
    expected = ('cat', 'cat1')
    assert actual == expected

def test_dequeue2():
    shelter = AnimalShelter()
    shelter.enqueue('dog','dog1')
    shelter.enqueue('dog','dog3')
    actual = shelter.dequeue('dog1')
    expected = ('dog', 'dog1')
    assert actual == expected
