def count_down(i):
    # base case
    if i <= 0:
        return 0
    # recursive case
    else:
        print(i)
        return count_down(i - 1)


count_down(10)

