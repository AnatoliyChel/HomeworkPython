# прочитал данные из файла построчно
in_file = open("hw-4_in.txt", "r")
in_data = in_file.readlines()
in_file.close()

# открываем\создаем новый файл
out_file = open("hw-4_out.txt", "a")

russian_numbers = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}

# пишем в новый файл построчно
for el in in_data:
    user_str = russian_numbers.get(el.split()[0])
    out_file.writelines(el.replace(el.split()[0], user_str))

out_file.close()




