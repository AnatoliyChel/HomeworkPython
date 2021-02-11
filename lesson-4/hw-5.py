from functools import reduce

def multi(a, b):
    return a * b

result_list = [el for el in range(100, 1002, 2)]

# print(result_list)
print(reduce(multi, result_list))
