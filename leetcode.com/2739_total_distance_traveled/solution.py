class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        d = 0

        while mainTank:
            d += 10
            mainTank -= 1

            if d % 50 == 0 and additionalTank:
                mainTank += 1
                additionalTank -= 1

        return d
