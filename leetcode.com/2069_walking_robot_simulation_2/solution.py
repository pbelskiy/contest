EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dir = EAST
        self.x = 0
        self.y = 0
        self.p = (width + height - 2) * 2

    def move(self, num: int) -> None:
        if num >= self.p:
            num %= self.p
            if self.x == 0 and self.y == 0 and self.dir == EAST:
                self.dir = SOUTH

        while num > 0:

            if self.dir == EAST:
                if self.x + num < self.width:
                    self.x += num
                    return

                num -= self.width - 1 - self.x
                self.x = self.width - 1
                self.dir = NORTH

            ###

            if self.dir == NORTH:
                if self.y + num < self.height:
                    self.y += num
                    return

                num -= self.height - 1 - self.y
                self.y = self.height - 1
                self.dir = WEST

            ###

            if self.dir == WEST:
                if self.x - num >= 0:
                    self.x -= num
                    return

                num -= self.x
                self.x = 0
                self.dir = SOUTH

            ###

            if self.dir == SOUTH:
                if self.y - num >= 0:
                    self.y -= num
                    return

                num -= self.y
                self.y = 0
                self.dir = EAST

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return {
            EAST: "East",
            NORTH: "North",
            WEST: "West",
            SOUTH: "South",
        }[self.dir]
