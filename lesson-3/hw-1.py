#задание 1
def div_two_num():
    a = float(input("Введите первое число"))
    b = float(input("Введите второе число"))
    if b!= 0:
        print(a/b)
    else:
        print("на ноль делить нельзя")

div_two_num()