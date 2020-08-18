def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):

        if arr[i] == target:
            return i
        



    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    hi = len(arr)
    lo = 0

    mid = (hi + lo) // 2

    if arr[mid] < target:

    elif arr[mid] > target:
        



    return -1  # not found
