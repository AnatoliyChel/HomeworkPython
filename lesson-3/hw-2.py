def save_user_data(**kvars):
    """Выводит на экран только значения именованных аргументов в одну строчку через пробелы"""
    result_text = ""
    for i, el in enumerate(kvars.values()):  # добавляем индекс для поиска последнего элемента
        result_text += el
        if i != len(kvars.values()) - 1:  # добавляем пробел для всех слов кроме последнего
            result_text += " "
    print(result_text)

user_data = input("Введите через пробел имя, фамилию, год рождения, город проживания, email, телефон - ").split()

save_user_data(имя=user_data[0], фамилия=user_data[1], год=user_data[2], город=user_data[3], \
               почта=user_data[4], телефон=user_data[5])



