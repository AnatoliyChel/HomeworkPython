# задание6
origin_list = [(1, {"название": "компьютер", "цена": 30000, "количество": 5, "ед": "шт"}), \
               (2, {"название": "принтер", "цена": 300, "количество": 10, "ед": "шт"})]
i = 3
while True:
    user_name = input("Введите название товара - ")
    user_price = int(input("Введите цену товара - "))
    user_count = int(input("Введите количество товара - "))
    user_unit = input("Введите единицы - ")

    # создаем единичный кортеж и добавляем в исходный список
    user_data = dict(название = user_name, цена = user_price, количество = user_count, ед= user_unit)
    temp_list = [i] # присваиваем порядковый номер товару
    i += 1
    temp_list.append(user_data)
    origin_list.append(tuple(temp_list)) # добавляем в главный

    # создаем пустые списки
    result_list1 = []
    result_list2 = []
    result_list3 = []
    result_list4 = []

    # перебираем исходный список и формируем из него сортированный словарь
    for el in origin_list:
        result_list1.append(el[1].get("название"))
        result_list2.append(el[1].get("цена"))
        result_list3.append(el[1].get("количество"))
        result_list4.append(el[1].get("ед"))

    # окончательный словарь
    result_dict = dict(название = result_list1, цена = result_list2, количество = result_list3, ед = result_list4)

    print(result_dict)


