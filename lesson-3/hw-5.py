result = 0.0

while True:
    user_string = input("Ведите строку чисел, разделенных пробелами или q для выхода").split()

    for el in user_string:
        if el == "q":
            break
        result += float(el)
    if result > 0.0:
        print(result)
    if el == "q":
        break



