from data_structures_and_algorithms.data_structures.linked_list.linked_list import Linkedlist
from data_structures_and_algorithms.data_structures.linked_list.linked_list import *
import pytest

def test_instance():
    ll = Linkedlist()
    assert isinstance(ll, Linkedlist)


def test_insert(prep_ll):
    assert prep_ll.head.value == 15
    assert prep_ll.head.next.value == 8
    assert prep_ll.head.next.next.value == 555
    assert prep_ll.head.next.next.next.value == 6
    assert prep_ll.head.next.next.next.next.value == 555
    assert prep_ll.head.next.next.next.next.next.value == 3
    assert prep_ll.head.next.next.next.next.next.next == None

def test_includes(prep_ll):
    assert prep_ll.includes(15)
    assert prep_ll.head.next.value == 8
    assert prep_ll.head.next.next.value != 10
    assert not prep_ll.includes(10)

def test_to_string(prep_ll):
    actual = prep_ll.to_string()
    expected = f' { {15} } -> { {8} } -> { {555} } -> { {6} } -> { {555} } -> { {3} } -> NULL'
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
    assert prep_ll.head.next.next.value == 555


def test_insertAfter(prep_ll):
    assert prep_ll.head.next.next.next.next.value == 555

    

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
