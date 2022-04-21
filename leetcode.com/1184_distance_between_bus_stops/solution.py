class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        s1 = sum(distance[start:destination])
        s2 = sum(distance) - s1
        return min(s1, s2)
