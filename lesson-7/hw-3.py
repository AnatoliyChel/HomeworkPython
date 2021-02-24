class Square:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Square(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells >= 0:
            return Square(self.cells - other.cells)
        else:
            print("сумма меньше нуля")
            return Square(0)

    def __mul__(self, other):
        return Square(self.cells * other.cells)

    def __truediv__(self, other):
        return Square(self.cells // other.cells)

    def make_order(self, cells):
        from math import ceil  # импортируем округление до целого
        result = ""
        i = 0
        for _ in range(ceil(self.cells/cells)):
            for _ in range(cells):
                if self.cells - i > 0:
                    result += "*"
                    i += 1
            result += "\n"
        return result


square1 = Square(6)
square2 = Square(5)

print(square1.make_order(5))

square3 = square1 + square2
print(square3.cells)

square4 = square1 - square2
print(square4.cells)

square5 = square1 * square2
print(square5.cells)

square6 = square1 / square2
print(square6.cells)