import re

# прочитал данные из файла построчно
in_file = open("hw-6.txt", "r")
in_data = in_file.readlines()
in_file.close()

result_dict = {}

for el in in_data:
    new_str = [int(re.findall(r"\d+", el1)[0]) for el1 in el.split()[1:] if el1 != "-"] # создаем список только из цифр
    # print(sum(new_str))
    new_key = {el.split()[0]: sum(new_str)} # формируем новый объект для словаря из строки
    result_dict.update(new_key)

print(result_dict)


