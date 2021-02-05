# задание5
raiting = [7,5,3,1]

while True:
    user_raiting = input("Введите новый элемент рейтинга")
    max_raiting = max(raiting)
    # print(max_raiting)
    if int(user_raiting) > max_raiting: # добавляем в начало самый максимальный
        raiting.insert(0, int(user_raiting))
    else: # если не максимальный то ищем похожий элемент
        if int(user_raiting) in raiting: # если элемент существует в списке
            raiting = list(reversed(raiting))  # переворачиваем список
            pos = raiting.index(int(user_raiting)) # позиция первого такого же элемента в перевернутом списке
            raiting.insert(pos + 1, int(user_raiting))
            raiting = list(reversed(raiting))  # переворачиваем список обратно
        else: # если элемента нет в списке то перебором ищем ему место
            for el in raiting:
                if el < int(user_raiting):
                    pos = raiting.index(el)
                    raiting.insert(pos, int(user_raiting))
                    break
    print(raiting)