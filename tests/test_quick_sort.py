from data_structures_and_algorithms.challenges.quick_sort.quick_sort import QuickSort,Partition,Swap
import pytest

def test_QuickSort():
    arr = [8,4,23,42,16,15]
    left = 0
    right = len(arr) - 1
    QuickSort(arr, left, right)
    expected = [4, 8, 15, 16, 23, 42]
    assert arr == expected

def test_few_uniques():
    arr = [20,18,12,8,5,-2]
    left = 0
    right = len(arr) - 1
    QuickSort(arr, left, right)
    expected = [-2, 5, 8, 12, 18, 20]
    assert arr == expected

def test_reverse_sorted():
    arr = [5,12,7,5,5,7]
    left = 0
    right = len(arr) - 1
    QuickSort(arr, left, right)
    expected = [5, 5, 5, 7, 7, 12]
    assert arr == expected

def test_nearly_sorted():
    arr = [2,3,5,7,13,11]
    left = 0
    right = len(arr) - 1
    QuickSort(arr, left, right)
    expected = [2, 3, 5, 7, 11, 13]
    assert arr == expected
