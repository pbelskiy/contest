class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.slots[carType - 1] -= 1
        return self.slots[carType - 1] >= 0
