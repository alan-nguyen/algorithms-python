def quicksort(array):
    """ Quick sort algorithm """
    # base case, array with 0 or 1 element are already sorted
    if len(array) < 2:
        return array
    # recursive case
    else:
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# test case
print(quicksort([9, 3, 12, 0, 200]))
