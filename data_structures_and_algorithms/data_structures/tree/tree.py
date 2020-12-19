class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None


    def preorder(self):
        output = []

        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output
    

    def inorder(self):
        output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
                
            output.append(node.value)
            
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output
    
    
    def postorder(self):
        output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            
            output.append(node.value)

        _walk(self.root)
        return output
    
# ************************************** BST ************************************************* #
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
        
    def add(self, value):
        if not self.root:
            self.root = Node(value)
            
        else:
            def _walk(node):
                if value < node.value:
                    # go left
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)
                
                else:
                    # go right
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)
                        
            _walk(self.root)


    def contains(self, value):
        output = []
        
        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root) 
        
        if value in output:
            return True
        else:
            return False



if __name__ == "__main__":
    bt = BinaryTree()
    bst = BinarySearchTree()
    print('*************** BT ****************')
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    print(bt.preorder())
    print(bt.inorder())
    print(bt.postorder())
    print('*************** BST ****************')
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    print(bst.contains(8))
