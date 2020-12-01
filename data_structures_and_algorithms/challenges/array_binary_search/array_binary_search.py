import math

def BinarySearch(arr, val):

    start = 0
    mid = None
    end = len(arr) -1

    while start <= end:
        
        mid = math.floor( (start + end) / 2 )

        if arr[mid] == val:
            return mid
        
        elif val < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
          
    return -1

print(BinarySearch([1,2,3,4,5,6], 3))
