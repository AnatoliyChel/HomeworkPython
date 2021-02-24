class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("запуск отрисовкм")


class Pen(Stationery):

    def draw(self):
        print("нарисован ручкой")


class Pencil(Stationery):
    def draw(self):
        print("нарисован карандашем")


class Handle(Stationery):
    def draw(self):
        print("нарисован маркером")


st1 = Stationery("stationary1")
print(st1.title)
st1.draw()

st2 = Pen("Pen1")
print(st2.title)
st2.draw()

st3 = Pencil("Pencil1")
print(st3.title)
st3.draw()

st4 = Handle("Handle1")
print(st4.title)
st4.draw()



