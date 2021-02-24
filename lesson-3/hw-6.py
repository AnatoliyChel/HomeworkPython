def int_func(user_string):
    return user_string.title()

user_text = input("Введите текст").lower().split()

result_text = ""
for i, el in enumerate(user_text): # добавляем индекс для поиска последнего элемента
    result_text += int_func(el)
    if i != len(user_text)- 1: # добавляем пробел для всех слов кроме последнего
        result_text += " "
print(result_text)