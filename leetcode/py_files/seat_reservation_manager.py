# design a system that manages the reservation state of n seats that are numbered from 1 to n
# implement the SeatManager class:
#   * SeatManager(int n) initializes a SeatManager object that will manage n seats numbered from 1 to n.
#      All seats are initially available
#   * int reserve() fetches the smallest-numbered unreserved seat, reserves it, and returns its number
#   * void unreserve(int seatNumber) unreserves the seat with the given seatNumber

class SeatManager:

    def __init__(self, n: int):
        self.seats = [False] * n
        self.free = 0

    def reserve(self) -> int:
        self.seats[self.free] = True
        ans = self.free + 1
        self.free += 1
        return ans  # нумерация начинается с 1

    def unreserve(self, seat_number: int) -> None:
        self.seats[seat_number - 1] = False
        if self.free >= seat_number - 1:
            self.free = seat_number - 1


if __name__ == '__main__':
    sm = SeatManager(5)
    print(sm.seats)
    print(sm.reserve())
    print(sm.seats)
    print(sm.reserve())
    print(sm.seats)
    print(sm.reserve())
    print(sm.seats)
    print(sm.unreserve(4))
    print(sm.seats)
    print(sm.reserve())
    print(sm.seats)