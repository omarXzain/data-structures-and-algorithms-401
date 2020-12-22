import pytest
from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree, Node, BinarySearchTree

def test_breadth_first():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    actual = bst.breadth_first(bst)
    expected = [4, 9, 6, 8, 5, -1, 3]
    assert actual == expected    