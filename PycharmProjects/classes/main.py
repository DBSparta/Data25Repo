import datetime
from datetime import date
today = date.today()


class Car:

    def __init__(self, colour, max_speed, price, year, model, mileage, mot):
        self.current_speed = 0
        self.colour = colour
        self.max_speed = max_speed
        self.price = price
        self.year = year
        self.model = model
        self.mileage = mileage
        self.mot = mot

    def accelerate(self, speed_to_accelerate):
        if self.current_speed + speed_to_accelerate > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed += speed_to_accelerate
        return self.current_speed

    def decelerate(self, speed_to_decelerate):
        if self.current_speed - speed_to_decelerate > 0:
            self.current_speed -= speed_to_decelerate
        else:
            self.current_speed = 0
        return self.current_speed

    def journey(self, time):
        self.mileage += int(self.current_speed * time / 60)
        return self.mileage

    def brake(self):
        self.current_speed = 0
        return self.current_speed

    def value(self):
        if self.price * 0.9 * (today.year - self.year + 1) - (self.price * 0.01 * int(self.mileage/1000)) > 0:
            self.price = self.price * 0.9 * (today.year - self.year + 1) - (self.price * 0.01 * int(self.mileage/1000)) > 0
            return self.price
        else:
            self.price = 0
            return self.price

    def honk(self):
        return 'honk honk'


car1 = Car('Red', 200, 20000, 2021, 'Ferrari', 1000, True)
print(car1.value())

print(__name__)




