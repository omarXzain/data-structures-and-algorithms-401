class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

class Hashtable:
    def __init__(self, size=1024):
        self.map = [None]*size
        self.size = size

    def hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total*19 % self.size

    def add(self, key, value):
        Hkey = self.hash(key)

        if self.map[Hkey] == None:
            self.map[Hkey] = LinkedList()
            self.map[Hkey].add([key , value])
            return
        
        if self.contains(key):
            current = self.map[Hkey].head
            while current:
                if current.data[0] == key :
                    current.data[1] = value
                current = current.next
            return           
        
        else:
            self.map[Hkey].add([key , value])
            return
        
        
    def get(self, key):
        Hkey = self.hash(key)
        if self.map[Hkey]:
            current = self.map[Hkey].head
            while current:
                if current.data[0] == key :
                    return current.data[1]
                current = current.next
            return 'key not exist'
        else:
            return 'key not exist'

    def contains(self, key):
        Hkey = self.hash(key)
        if self.map[Hkey]:
            current = self.map[Hkey].head
            while current:
                if current.data[0] == key :
                    return True
                current = current.next
            return False
        else:
            return False

if __name__=='__main__':
    people = LinkedList()
    people.add('omar')
    people.add('zain')
    people.add('saed')
    people.add('saleh')
    assert people.head.data == 'omar'
    assert people.head.next.data == 'zain'
    assert people.head.next.next.data == 'saed'
    assert people.head.next.next.next.data == 'saleh'
    print('passed')
    hash = Hashtable()
    hash.add('HI',30)
    print(hash.get('HI'))