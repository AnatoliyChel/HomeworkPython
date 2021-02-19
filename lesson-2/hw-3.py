# задание3
# решение через list
months = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
seasons = ["зима", "весна", "лето", "осень"]

while True:
    user_month = input("Введите номер месяца, нажмите q для выхода")
    if str(user_month) == "q":
        break
    result = seasons[months.index(int(user_month)) // 3]
    print(result)

# решение через dictionary, закоментировать весь предыдущий код перед запуском
# seasons = {12: "зима", 1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", \
#             9: "осень", 10: "осень", 11: "осень"}
#
# result = seasons.get(int(input("Введите номер месяца")))
# if result is None:
#     print("Вы ввели неправильный номер")
# else:
#     print(result)