def reverse_array(arr):
    """Reverses a list
    Args:
        arr (list): python list
    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here

    newArr = []
    for x in arr:
        newArr.append(arr[len(arr) - x])
    return newArr


print(reverse_array([1, 2, 3, 4, 5, 6]))
