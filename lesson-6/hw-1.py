class TrafficLight:
    __color = "red"
    __colors = (["red", 7], ["yellow", 2], ["green", 5]) # цвет и его продолжительность

    def running(self):
        import time
        for color, length in TrafficLight.__colors:
            TrafficLight.__color = color
            print(color)
            time.sleep(length)


tl1 = TrafficLight()
while True:
    tl1.running()