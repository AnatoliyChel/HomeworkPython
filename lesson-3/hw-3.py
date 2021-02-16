def my_func(a, b, c):
    if a > b:
        max1 = a
        if b > c:
            max2 = b
        else:
            max2 = c
    elif a < b:
        max1 = b
        if a < c:
            max2 = c
        else:
            max2 = a
    return max1 + max2

print(my_func(5,3,6))