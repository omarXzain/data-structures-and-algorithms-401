from data_structures_and_algorithms.data_structures.linked_list.linked_list import Linkedlist

def reverse( linkedlist):
    arr = []
    current = linkedlist.head
    
    while current:
        arr.append(current.value)
        current = current.next
        
    reversedArr = []
    while arr != []:
        reversedArr.append(arr.pop())
        
    return reversedArr


if __name__ == "__main__":
    li=Linkedlist()
    li2=Linkedlist()
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(9)
    li.append(10)
    li.append(11)
    li2.append(9)
    li2.append(10)
    li2.append(11)
    print(li.to_string())
    print('reverse: ', reverse(li))