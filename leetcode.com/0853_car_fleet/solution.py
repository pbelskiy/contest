"""
Sort cars by their positions, then from the end calculate time
to be at finish point.

TC: O(NlgN) -- sort
SC: O(lgN) -- sort
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        position, speed = zip(*sorted(zip(position, speed), reverse=True))

        time_next = (target - position[0]) / speed[0]

        for i in range(1, len(position)):
            time_curr = (target - position[i]) / speed[i]

            # so, out car is faster, we catch up with next car
            if time_curr <= time_next:
                continue

            fleets += 1
            time_next = time_curr

        return fleets
