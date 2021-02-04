#задание 1
# num = 10
# num_f = 2.5
# print(num, num_f)
#
# num1_user = input("Введите число 1 - ")
# num2_user = input("Введите число 2 - ")
# str_user = input("Введите строку")
#
# print("Число 1 - ", num1_user, "\n", "Число 2 - ", num2_user, "\n", "Строка - ", str_user)

#задание 2
# user_time = int(input("Введите время в с "))
# hours = user_time // 3600
# minutes = (user_time % 3600) // 60
# seconds = (user_time % 3600) % 60
# # 0 - символ заполнитель, > выравнивание по правому краю, 2 кол-во символов
# print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")

#задание 3
# n = input("Введите число:")
# nn = int(n + n)
# nnn = int(n + n + n)
# n = int(n)
# print(n + nn + nnn)

#задание 4
# user_num = input("Введите целое положительное многозначное число:")
# i = 0 #порядковый номер цифры внутри числа
# max_num = int(user_num[i])  # max number
#
# while i < len(user_num) - 1:
#     if max_num < int(user_num[i + 1]):
#         max_num = int(user_num[i + 1])
#     i = i + 1
# print("Максимальная цифра - ", max_num)

#задание 5
# viruchka = int(input("Введите значение выручки"))
# izderzki = int(input("Введите значение издержек"))
# pribil = viruchka - izderzki
# if pribil > 0:
#     print("Вы работаете с прибылью")
#     print("Ваша ренетабельность - ", pribil / viruchka)
#     people_num = int(input("Введите численность сотрудников"))
#     print("Прибыль на одного сотрудника - ", pribil / people_num)
# else:
#     print("Вы работатет в убыток")

#задание 6
result1 = int(input("Введите результат первого дня - "))
result2 = int(input("Введите требуемый результат - "))

current_day = 1
result_sum = result1
while result_sum < result2:
    print(current_day, "-й день", result_sum)
    result_sum = result_sum + (result_sum * 0.1)
    current_day = current_day + 1

print(current_day, "-й день", result_sum)
print("На", current_day, "-й день спортсмен достиг результата не менее", result2)



