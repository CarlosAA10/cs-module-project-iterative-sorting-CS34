# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for unsorted_index in range(cur_index, len(arr)):
            # if we find a value < smallest_index element,
            # update our smallest_index variable
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index

            # we've found the smallest element in the unsorted portion
            # swap it with the element right next to the cur_index
        arr[smallest_index] , arr[cur_index] = arr[cur_index] , arr[smallest_index]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    swaps_occurred = True

    while swaps_occurred:
        swaps_occurred = False

        for i in range (0, len(arr) - 1):
            #compare two elements
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
