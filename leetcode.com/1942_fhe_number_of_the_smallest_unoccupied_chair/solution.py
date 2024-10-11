"""
Simple greedy process simulation, with heapq and set
for performance boost.

- Sort times by arrival
- Before give new chair, using heapq free given chairs
- Then using set and heapq find the next minimal chair

TC: O(NlgN)
SC: O(N)
"""
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        leave = []
        occupied = set()

        free = list(range(len(times)))
        heapify(free)

        for arrival, leaving, i in sorted([(*t, i) for i, t in enumerate(times)]):

            # check for leaving
            while leave:
                time, chair = heappop(leave)
                if time > arrival:
                    heappush(leave, (time, chair))
                    break

                # free chair of left friend
                occupied.remove(chair)
                heappush(free, chair)

            # give minimal chair for new arrived friend
            while free:
                chair = heappop(free)
                if chair not in occupied:
                    break

            if i == targetFriend:
                return chair

            occupied.add(chair)
            heappush(leave, (leaving, chair))
