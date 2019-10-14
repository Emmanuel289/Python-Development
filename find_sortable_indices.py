""" function that returns a pair of indices m,n such that if the elements of an array were
sorted from m to n, the whole array would be sorted
E.g.
Input:  1,2,4,7,10,7,11,12,6,7,16,18,19
Expected Output: (3,9)
Input: 10,9,8,7,6,5
Expected Output: (0,5)

Special thanks to Anthony D.Mays (https://anthonydmays.com), a software engineer at Google who provided the material for
the logic and the javascript program on his Youtube channel( Name:Anthony D. Mays)
"""

import math


def find_sortable_indices(arr):
    i = 1
    start = None
    end = None
    largest_value = arr[0]
    min_unsorted = math.inf
    if not arr or len(arr) == 0 or len(arr) == 1:
        return []
    while i < len(arr):
        if arr[i] < largest_value:
            if not start:
                start = i
            end = i
        else:
            largest_value = arr[i]

            if start and arr[i] < min_unsorted:
                min_unsorted = arr[i]
        i += 1
    if not start:
        return []
    for i in range(0, start):
        if arr[i] < min_unsorted:
            start = i
    return start, end


# test function to see if it returns the correct indices
test_array1 = [1, 2, 4, 7, 10, 7, 11, 12, 6, 7, 16, 18, 19]
test_array2 = [10, 9, 8, 7, 6, 5]
print(find_sortable_indices(test_array1))
print(find_sortable_indices(test_array2))
