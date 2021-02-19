from itertools import count, cycle

# start = int(input("Введите начальное значение"))
# for el in count(start):
#     if el > start + 20:
#         break
#     else:
#         print(el)


orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, j in enumerate(cycle(orig_list)):
    if i > 10:
        break
    else:
        print(j)
