
class Car:
    def __init__(self, make = "Dommestic", year = 2018):
        self.make = make
        self.year = year

    def age(self):
        return 2022 - self.year

carAge = Car()

print(carAge.age())
