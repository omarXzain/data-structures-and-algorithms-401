from data_structures_and_algorithms.data_structures.linked_list.linked_list import Linkedlist


def zip_lists(list1, list2):
    finalList = Linkedlist()
    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        finalList.append(current1.value)
        finalList.append(current2.value)
        current1 = current1.next
        current2 = current2.next
    return finalList


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
    print(li2.to_string())
    print('final: ',zip_lists(li,li2).to_string())
