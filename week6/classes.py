#!/usr/bin/env python3
import sys
class Car:
    def __init__(self, name, year):
        self.gear = 0
        self.max_gear = 5
        self.name = name
        self.year = year
    def gear_up(self):
        if self.gear <= self.max_gear:
            self.gear += 1
        
    def gear_down(self):
        if self.gear > 0:
            self.gear -= 1

    def print_car(self):
        sys.stdout.write(f"Car {self.name} of year {self.year} is on gear {self.gear}")
        # print(f"Car {self.name} of year {self.year} is on gear {self.gear}")

car = Car("Golf", "2015")
car.gear_up()
car.gear_up()
car.gear_down()
car.print_car() # out: Car Golf of year 2015 is on gear 1
sys.stdout.flush()