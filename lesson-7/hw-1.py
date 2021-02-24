class Matrix:
    def __init__(self, *args):
        self.arg = args
        self.str = ""
        self.columns = len(self.arg[0])
        self.rows = len(self.arg)
        self.__sum = []
        self.__row = []

    def __str__(self):  # отображение матрицы на экране
        for el in self.arg:
            for el2 in el:
                self.str += str(el2) + " "
            self.str += "\n"
        return self.str

    def __add__(self, other):  # сложение двух матриц
        self.__sum = []
        if self.columns == other.columns and self.rows == other.rows:  # сравниваем размер матриц
            for row1, row2 in zip(self.arg, other.arg):  # перебераем строки
                for col1, col2 in zip(row1, row2):  # перебираем колонки
                    self.__row.append(col1 + col2)
                self.__sum.append(self.__row)
                self.__row = []
            return Matrix(*self.__sum)  # передаем в качестве аргументов распакованный список
        else:
            print("разный размер матриц")
            return Matrix(0)


mat1 = Matrix([100, 200, 300], [400, 500, 600], [700, 800, 900])
print(mat1)

mat2 = Matrix([-10, -20, -30], [-40, -50, -60], [70, 80, 90])
print(mat2)

mat3 = mat1 + mat2
print(mat3)