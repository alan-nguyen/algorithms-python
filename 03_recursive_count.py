def count_recusive(list):
    """ Count the number of elements in list """
    if list == []:
        return 0
    return 1 + count_recusive(list[1:])


# test case
print(count_recusive([1, 2, 4, 6]))