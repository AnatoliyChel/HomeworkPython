# задание2
my_list = []

while True:
    my_list.append(int(input("Введите число")))
    print("Исходный порядок ", my_list)
    if len(my_list) > 1:
        for index, el in enumerate(my_list):
            if (index % 2) != 0: # определяем нечетный индекс
                my_list[index], my_list[index - 1] = my_list[index - 1], my_list[index]
        print("Измененый порядок", my_list)
