class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        index = 0
        delta = 0

        for i, (a, b) in enumerate(zip(releaseTimes, [0] + releaseTimes[:])):
            d = a - b
            if d > delta or d == delta and keysPressed[i] > keysPressed[index]:
                delta = d
                index = i

        return keysPressed[index]
