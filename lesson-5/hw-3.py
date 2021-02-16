out_file = open("hw-3.txt", "r")
out_data = out_file.readlines()
out_file.close()

for el in out_data:
    oklad = int(el.split()[1])
    if oklad < 20000:
        print(el.split()[0], oklad * 12) # не понял, что такое средняя величина дохода. Вывел за год


