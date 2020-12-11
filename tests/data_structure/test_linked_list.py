from data_structures_and_algorithms.data_structures.linked_list.linked_list import Linkedlist
from data_structures_and_algorithms.data_structures.linked_list.linked_list import *
from data_structures_and_algorithms.data_structures.ll_zip import zip_lists 
import pytest

def test_instance():
    ll = Linkedlist()
    assert isinstance(ll, Linkedlist)


def test_insert(prep_ll):
    assert prep_ll.head.value == 3
    assert prep_ll.head.next.value == 555
    assert prep_ll.head.next.next.value == 6
    assert prep_ll.head.next.next.next.value == 555
    assert prep_ll.head.next.next.next.next.value == 8
    assert prep_ll.head.next.next.next.next.next.value == 15
    assert prep_ll.head.next.next.next.next.next.next == None

def test_includes(prep_ll):
    assert prep_ll.includes(15)
    assert prep_ll.head.next.value == 555
    assert prep_ll.head.next.next.value != 10
    assert not prep_ll.includes(10)

def test_to_string(prep_ll):
    actual = prep_ll.to_string()
    expected = f' { {3} } -> { {555} } -> { {6} } -> { {555} } -> { {8} } -> { {15} } -> NULL'
    assert actual == expected


def test_append():
    ll = Linkedlist()
    ll.append(5)
    assert ll.head.value == 5


def test_append2():
    ll = Linkedlist()
    ll.append('a')
    ll.append('b')
    assert ll.head.value == 'a'
    assert ll.head.next.value == 'b'
    

def test_insertBefore(prep_ll):
    assert prep_ll.head.next.next.next.value == 555


def test_insertAfter(prep_ll):
    assert prep_ll.head.next.next.next.next.next.value == 15


def test_kth_from_end(prep_ll):
    actual = prep_ll.ll_kth_from_end(0)
    expected = 15
    assert actual == expected


def test_kth_from_end2(prep_ll):
    actual = prep_ll.ll_kth_from_end(2)
    expected = 555
    assert actual == expected
    

def test_kth_from_end3(prep_ll):
    actual = prep_ll.ll_kth_from_end(6)
    expected = 'Exception'
    assert actual == expected


def test_zip_2nd_empty():
    list1 = Linkedlist()
    list2 = Linkedlist()
    list1.append(1)
    list1.append(2)
    list2.append(3)
    list2.append(4)
    actual = zip_lists(list1, list2)
    assert actual.to_string() == " {1} -> {3} -> {2} -> {4} -> NULL"

def test_zip_same_length():
    list1 = Linkedlist()
    list2 = Linkedlist()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(4)
    list2.append(5)
    list2.append(6)
    actual = zip_lists(list1, list2)
    assert actual.to_string() == " {1} -> {4} -> {2} -> {5} -> {3} -> {6} -> NULL"

def test_zip_1st_longer():
    list1 = Linkedlist()
    list2 = Linkedlist()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(4)
    list2.append(5)
    actual = zip_lists(list1, list2)
    assert actual.to_string() == " {1} -> {4} -> {2} -> {5} -> NULL"

def test_zip_2nd_longer():
    list1 = Linkedlist()
    list2 = Linkedlist()
    list1.append(1)
    list2.append(4)
    list2.append(5)
    list1.append(2)
    actual = zip_lists(list1, list2).to_string()
    expected =  " {1} -> {4} -> {2} -> {5} -> NULL"
    assert  actual == expected
    
@pytest.fixture
def prep_ll():
    list1 = Linkedlist()
    list1.insert(15)
    list1.insert(8)
    list1.insert(6)
    list1.insert(3)

    list1.includes(15)
    list1.includes(8)
    list1.includes(10)

    list1.insertBefore(555, 6)
    list1.insertAfter(555, 6)

    list1.to_string()
    return list1
