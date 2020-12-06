from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import *

def test_BinarySearch():
    arr = [ 25, 35, 65, 80, 85,86,96,97,98,102,112 ] 
    target = 85
    actual = BinarySearch( arr, target )
    expected = 4
    
    assert actual == expected

def test_BinarySearch():
    arr = [ 25, 35, 65, 80, 85,86,96,97,98,102,112 ] 
    target = 212
    actual = BinarySearch( arr, target )
    expected = -1
    assert actual == expected