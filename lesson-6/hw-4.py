class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("car is running")

    def stop(self):
        print("car is stopped")

    def turn(self, direction):
        print(f"{self.name} turned {direction}")

    def show_speed(self):
        print(f"{self.name} - {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("over speed")
        else:
            Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("over speed")
        else:
            Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


car1 = Car("car", "red", 80, True)
car1.show_speed()

car2 = TownCar("TownCar", "blue", 70, False)
car2.show_speed()

car3 = SportCar("SportCar", "orange", 100, False)
car3.show_speed()
car3.turn("right")

car4 = WorkCar("WorkCar", "black", 50, False)
car4.show_speed()

car5 = PoliceCar("PoliceCar", "blue", 70)
car5.show_speed()


