import json

# прочитал данные из файла построчно
in_file = open("hw-7_in.txt", "r")
in_data = in_file.readlines()
in_file.close()

result_list = []
i = 0 # количество фирм с прибылью
average_profit = 0.0
user_dict = {}
for el in in_data:
    pribyl = int(el.split()[2]) - int(el.split()[3])
    user_dict.update({el.split()[0]: pribyl})
    if pribyl >= 0: # добавляем в среднее если прибыль больше равно нулю
        average_profit = (average_profit + pribyl)
        i += 1
result_list.append(user_dict)
result_list.append({"average_profit": average_profit / i})

print(result_list)

with open("hw-7_out_json", "w") as out_f:
    json.dump(result_list, out_f)

