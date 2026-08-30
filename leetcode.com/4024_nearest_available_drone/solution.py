class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        m = float('-inf')
        v = float('inf')

        for i, (x, y, r) in enumerate(drones):
            d = abs(x - tx) + abs(y - ty)
            if d > r:
                continue

            if d < v:
                v = d
                m = i
        
        return m if m != float('-inf') else -1

