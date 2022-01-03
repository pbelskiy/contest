class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        t, l, r = 0, 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                t += 1
                l += 1
                r -= 1
            else:
                t += 1
                r -= 1

        return t
