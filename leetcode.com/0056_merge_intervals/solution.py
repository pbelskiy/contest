from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        intervals = sorted(intervals, key=lambda k: k[0])
        result.append(intervals[0])

        for interval in intervals[1:]:
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result


if __name__ == '__main__':
    s = Solution()

    assert s.merge([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
