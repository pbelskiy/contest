class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        t = 0

        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    t += 1

        return t
