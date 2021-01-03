from data_structures_and_algorithms.challenges.insertion_sort.insertion_sort import *
import pytest

def test_insertion_sort():
    list1 = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    InsertionSort(list1)
    assert list1 == expected

def test_insertionSort2():
    list1 = [20, 41, 3, 2, 16, 10]
    expected = [2, 3, 10, 16, 20, 41]
    InsertionSort(list1)
    assert list1 == expected
