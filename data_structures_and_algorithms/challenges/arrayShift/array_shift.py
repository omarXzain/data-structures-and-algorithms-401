import math


def insertShiftArray(arr, val):

    i = math.ceil(len(arr)/2)

    print(arr[:i] + [val] + arr[i:])

    return(arr[:i] + [val] + arr[i:])


insertShiftArray([1, 2, 3, 4, 5, 6], 10)
