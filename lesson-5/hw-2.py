user_file = open("hw-2.txt", "r")
str_content = user_file.readlines() # делаем список из построчнорго чтения файла
user_file.close()
print(f"Всего строк -  {len(str_content)}")
for el in str_content:
    print(f"Количество слов в строке - {len(el.split())}")

