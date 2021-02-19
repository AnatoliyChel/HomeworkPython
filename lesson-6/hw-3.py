class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {
            "wage": wage,
            "bonus": bonus,
        }


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(sum(self._Worker__income.values()))


man1 = Position("name1", "surname1", "position1", 10, 20)
man2 = Position("name2", "surname2", "position2", 20, 30)

man1.get_full_name()
man1.get_total_income()
man2.get_full_name()
man2.get_total_income()
