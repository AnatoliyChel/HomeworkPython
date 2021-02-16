
while True:
    user_str = input("Введите что нибудь. Пустая строка - конец ввода")
    if user_str == " ":
        break
    else:
        new_file = open("out_file.txt", "a")
        new_file.writelines(user_str + "\n")
        new_file.close()



