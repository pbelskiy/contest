class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps, curr, i = 0, capacity, 0

        while i < len(plants):
            if plants[i] > curr:
                steps += i*2
                curr = capacity

            curr -= plants[i]
            steps += 1
            i += 1

        return steps
