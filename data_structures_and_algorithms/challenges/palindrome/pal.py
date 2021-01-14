

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class LinkedList: 
    def __init__(self): 
        self.head = None


#=========================================

    def palindrome(self):
        node = self.head
        arr = []
        while node:
            arr.append(node.data)
            node = node.next

        node = self.head
        for element in arr[::-1]:
            if (element != node.data):
                return False 
            node = node.next
        return True


#==========================================

if __name__ == "__main__":
    ll = LinkedList() 
    ll.head = Node('m') 
    ll.head.next = Node('x') 
    ll.head.next.next = Node("o") 
    ll.head.next.next.next = Node("o")
    ll.head.next.next.next.next = Node("xvvv") 
    ll.head.next.next.next.next.next = Node("m") 
    print (ll.palindrome())
    #     print("TRUE")
    # else:
    #     print("FALSE")




