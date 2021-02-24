# создаем новый файл с списком чисел через пробел
out_file = open("hw-5_out.txt", "a")
user_list = [str(el) for el in range(10)]
out_file.writelines(" ".join(user_list))
out_file.close()

# читаем созданный файл
in_file = open("hw-5_out.txt", "r")
in_data = in_file.read()
in_file.close()

# выводим на экран сумму чисел из файла, преобразовав их из str в int
in_file_int = [int(el) for el in in_data.split()]
print(sum(in_file_int))
