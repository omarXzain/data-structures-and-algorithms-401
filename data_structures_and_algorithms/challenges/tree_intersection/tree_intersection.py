from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree ,Node

def tree_intersection(tree1,tree2):
    output = []
    if tree1.root and tree2.root:
        array1 = tree1.preorder()
        array2 = tree2.preorder()

        set2 = set(array2)
        for i in array1:
            if i in set2:
                output.append(i)
    return output



if __name__ == "__main__":
    tr1=BinaryTree()
    tr2 = BinaryTree()
    tr1.root = Node(7)
    tr1.root.right = Node(10)
    tr1.root.left = Node(-2)
    tr1.root.right.left = Node(5)
    tr1.root.left.left = Node(17)
    tr2.root = Node(5)
    tr2.root.right = Node(11)
    tr2.root.left = Node(-2)
    tr2.root.right.left = Node(12)
    tr2.root.left.left = Node(11)
    print(tree_intersection(tr1,tr2))