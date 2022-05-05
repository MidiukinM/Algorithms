# design a parking system for a parking lot
# the parking lot has three kinds of parking spaces: big, medium and small, with a fixed number of slots for each size
# implement the parking system class:
#   * ParkingSystem class gives the number of slots for each parking space
#   * add_car function gets a cartype (big:1, medium:2, small:3 respectively).
#     A car can only park in a parking space of its cartype.
#     return False if there is no space available, else park the car and return True

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.car_places = {1: big, 2: medium, 3: small}

    def add_car(self, cartype: int) -> bool:
        self.car_places[cartype] -= 1
        return self.car_places[cartype] >= 0


if __name__ == '__main__':
    ps = ParkingSystem(1, 1, 0)
    for cartype in [1, 2, 3, 1]:
        print(ps.add_car(cartype))