import pytest
from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree, Node, BinarySearchTree

def test_preorder(prep):
    actual = prep.preorder()
    expected = [6,-1,10,5,7,3]
    assert actual == expected
    
def test_inorder(prep):
    actual = prep.inorder()
    expected = [10, -1, 6, 7, 5, 3]
    assert actual == expected
    
def test_postorder(prep):
    actual = prep.postorder()
    expected = [10, -1, 7, 3, 5, 6]
    assert actual == expected

@pytest.fixture
def prep():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    return bt

def test_add():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    assert bst.root.value == 4
    assert bst.root.left.value == -1
    assert bst.root.right.value == 9
    assert bst.root.left.right.value == 3
    assert bst.root.right.left.left.value == 5
    
    
def test_contains():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    actual = bst.contains(9)
    expected = True
    assert actual == expected
    
    
def test_contains2():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    actual = bst.contains(12)
    expected = False
    assert actual == expected