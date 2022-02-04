class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Create for each delta list of points, two edged points will
        have maxium length on this delta.
        """
        t = 0
        d = collections.defaultdict(list)

        # add points to plot
        d[t].append(0)
        for i, n in enumerate(nums):
            if n == 0:
                t -= 1
            else:
                t += 1

            d[t].append(i + 1)

        # find maximum delta
        m = 0
        for v in d.values():
            m = max(m, v[-1] - v[0])

        return m
