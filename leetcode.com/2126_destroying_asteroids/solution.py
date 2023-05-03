class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for n in asteroids:
            if mass < n:
                return False

            mass += n

        return True
