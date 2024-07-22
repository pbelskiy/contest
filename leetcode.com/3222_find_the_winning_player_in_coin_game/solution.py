class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        while True:
            if x < 1 or y < 4:
                return 'Bob'

            x -= 1
            y -= 4

            if x < 1 or y < 4:
                return 'Alice'

            x -= 1
            y -= 4
