orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_list = [el for i, el in enumerate(orig_list) if i != 0 and el > orig_list[i - 1]]

print(result_list)

