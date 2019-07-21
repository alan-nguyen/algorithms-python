def sum_recursive(list):
    """ Sum function using recursive """
    if list == []:
        return 0
    return list[0] + sum_recursive(list[1:])


# test case
print(sum_recursive([1, 2, -1, 2]))
