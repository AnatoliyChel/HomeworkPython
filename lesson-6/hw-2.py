class Road:

    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width
        self.__height = 0
        self.__mass = 0

    def get_mass(self, mass, height):
        self.__height = height
        self.__mass = mass
        print(f"{(self.__length * self.__width * self.__height * self.__mass) / 1000} т")


r1 = Road(20, 5000)
r1.get_mass(25, 5)
