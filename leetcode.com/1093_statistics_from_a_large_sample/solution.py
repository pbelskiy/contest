"""
Just use 5 times each value using O(N) algo.

TC: O(N):
SC: O(1)
"""
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # find minimum O(N)
        minimum = 0
        for k in range(len(count)):
            if count[k] > 0:
                minimum = k
                break

        # find maximum O(N)
        maximum = 0
        for k in range(len(count) - 1, -1, -1):
            if count[k] > 0:
                maximum = k
                break

        # find mean O(N)
        total = 0
        length = 0
        for k in range(len(count)):
            total += k*count[k]
            if count[k] > 0:
                length += count[k]
        mean = total / length

        # find median O(N)
        median = 0
        index = 0
        prev = 0

        for k in range(len(count)):
            if index + count[k] <= length // 2:
                index += count[k]
                if count[k] > 0:
                    prev = k
                continue

            if length % 2 == 1:
                median = k
            elif index < length // 2 < index + count[k]:
                median = k
            else:
                median = (k + prev) / 2

            break

        # find mode O(N)
        mode = 0
        m = 0
        for k in range(len(count)):
            if count[k] > m:
                m = count[k]
                mode = k

        return [minimum, maximum, mean, median, mode]
