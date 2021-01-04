from data_structures_and_algorithms.challenges.merge_sort.merge_sort import Mergesort
import pytest

def test_reverse_sorted(arr1):  
    Mergesort(arr1)
    assert arr1 == [-2, 5, 8, 12, 18, 20]

def test_few_uniques(arr2):  
    Mergesort(arr2)
    assert arr2 == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted(arr3):  
    Mergesort(arr3)
    assert arr3 == [2, 3, 5, 7, 11, 13]

@pytest.fixture
def arr1():
    arr1 = [20,18,12,8,5,-2]
    return arr1

@pytest.fixture
def arr2():
    arr2 = [5,12,7,5,5,7]
    return arr2

@pytest.fixture
def arr3():
    arr3 = [2,3,5,7,13,11]
    return arr3