# Activity 1: Design Your Own Class
# We'll create a Superhero class as an example for this assignment.

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
        self.energy = 100

    def use_power(self):
        if self.energy > 10:
            print(f"{self.name} uses {self.power}!")
            self.energy -= 10
        else:
            print(f"{self.name} is too tired to use {self.power}.")

    def rest(self):
        print(f"{self.name} is resting...")
        self.energy = 100

# Inheritance Example
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        if self.energy > 20:
            print(f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!")
            self.energy -= 20
        else:
            print(f"{self.name} is too tired to fly.")
