# Activity 2: Test and demonstrate polymorphism with vehicles
from vehicles import Vehicle, Car, Plane, Boat

def main():
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()

if __name__ == "__main__":
    main()
