from sys import argv

def zarplata(hours, stavka, premia):
    print(f"Ваша зарплата: {hours * stavka + premia}")

zarplata(int(argv[1]), int(argv[2]), int(argv[3]))