from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree


def fizz_buzz_tree(k_ary):
    tree = BinaryTree()
    if not k_ary.root: return tree

    def _walk(current):
        node = Node(comapre(current.value))

        if current.left: node.left = _walk(current.left)
        if current.right: node.right = _walk(current.right)
        return node

    tree.root = _walk(k_ary.root)
    return tree


def comapre(num):
    if num % 3 == 0 and num % 5 == 0: return "FizzBuzz"
    elif num % 3 == 0: return "Fizz"
    elif num % 5 == 0: return "Buzz"
    elif num % 3 != 0 and num % 5 != 0: return num
    else: return str(num)
    


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(5)
    bt.root.right = Node(9)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(18)
    bt.root.right.right = Node(15)
    print(fizz_buzz_tree(bt).preorder())