
def Mergesort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        
        Mergesort(left) # sort the left side
        
        Mergesort(right) # sort the right side
        
        Merge(left, right, arr) # merge the sorted left and right sides together

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j +=  1
            
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
if __name__ == "__main__":
    temp = [8,4,23,42,16,15]
    Mergesort(temp)
    print(temp)