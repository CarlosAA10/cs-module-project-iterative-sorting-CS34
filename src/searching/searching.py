def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):

        if arr[i] == target:
            return i
        



    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    hi = len(arr) -1
    lo = 0

    while lo <= hi:

        mid = (lo + hi) // 2 # finds the middle point

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1






    return -1  # not found
