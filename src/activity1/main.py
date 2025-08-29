# Activity 1: Test and demonstrate the Superhero classes
from classes import Superhero, FlyingSuperhero

def main():
    hero1 = Superhero("Shadow Ninja", "Invisibility", "Metro City")
    hero2 = FlyingSuperhero("Sky Queen", "Wind Blast", "Cloud City", 500)

    hero1.use_power()
    hero1.use_power()
    hero1.rest()
    hero1.use_power()

    hero2.use_power()
    hero2.use_power()
    hero2.rest()
    hero2.use_power()

if __name__ == "__main__":
    main()
