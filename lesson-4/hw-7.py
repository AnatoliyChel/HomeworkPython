def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

# g = fact(5)

for el in fact(5):
    print(el)




