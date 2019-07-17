def find_smallest(arr):
    """ Find the smallest value in an array """
    # Store the smallest values
    smallest = arr[0]

    # Store the index of the smallest values
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index


def selection_sort(arr):
    """ Sort array """
    new_array = []
    for i in range(len(arr)):
        # Find the smallest element in the array and adds it to the new array
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array


print(selection_sort([4, 1, 6, 18, 9, 20]))