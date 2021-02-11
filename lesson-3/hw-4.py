# метод 1
# def my_func(x, y):
#     return x ** y


# метод 2 закоментируйте предыдущий код перед выполнением
def my_func(x, y):
    result = 1
    for el in range(abs(y)):
        result *= 1/x
    return result

x1 = int(input("Введите действительное положительное число"))
y1 = int(input("Введите отрицательную степень"))

print(my_func(x1, y1))
