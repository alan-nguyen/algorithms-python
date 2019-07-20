def max_r(list):
    """ Find the maximum value in the list """
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    else:
        sub_max = max_r(list[1:])
        return list[0] if list[0] > sub_max else sub_max


# test case
print(max_r([1, 0, 9, 20, 100])) # Should be 100

print(max_r([])) # Should be None

print(max_r([10])) # Should be 10