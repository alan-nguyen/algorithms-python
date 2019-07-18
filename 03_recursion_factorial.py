def fact(x):
    """Calculate factorial using recursion"""

    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(5))
