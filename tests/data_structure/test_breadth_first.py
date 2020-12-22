import pytest
from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree, Node, BinarySearchTree

def test_breadth_first_bst():
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
    
def test_breadth_first_bt():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    actual = bt.breadth_first(bt)
    expected = [6, 5, 3, 7, -1, 10]
    assert actual == expected
    
    
def test_breadth_first_bt2():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(7)
    bt.root.left = Node(6)
    bt.root.right.left = Node(2)
    bt.root.left.left = Node(9)
    bt.root.right.right = Node(5)
    actual = bt.breadth_first(bt)
    expected = [2,7,5,2,6,9]
    assert actual == expected   