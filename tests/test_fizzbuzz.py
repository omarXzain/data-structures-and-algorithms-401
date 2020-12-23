from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree
from data_structures_and_algorithms.data_structures.tree.FIZZBUZZTREE import fizz_buzz_tree

def test_fizz_buzz_tree():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(5)
    bt.root.right = Node(9)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(18)
    bt.root.right.right = Node(15)
    actual = fizz_buzz_tree(bt).preorder()
    expected = [1, 'Buzz', 2, 'Fizz', 'Fizz', 'FizzBuzz']
    assert actual == expected
    
    
def test_fizz_buzz_tree2():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(4)
    bt.root.left.left = Node(13)
    bt.root.left.right = Node(7)
    bt.root.right.right = Node(8)
    bt.root.right.right = Node(17)
    actual = fizz_buzz_tree(bt).preorder()
    expected = [1, 2, 13, 7, 4, 17]
    assert actual == expected
    
    
def test_fizz_buzz_tree3():
    bt = BinaryTree()
    bt.root = Node(3)
    bt.root.left = Node(5)
    bt.root.right = Node(6)
    bt.root.left.left = Node(9)
    bt.root.right.right = Node(15)
    actual = fizz_buzz_tree(bt).preorder()
    expected = ['Fizz', 'Buzz', 'Fizz', 'Fizz', 'FizzBuzz']
    assert actual == expected