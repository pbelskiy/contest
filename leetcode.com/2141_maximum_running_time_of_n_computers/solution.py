"""
We focus on n biggest batteries, then distribute rest of 
batteries over biggest ones evenly.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if len(batteries) == n:
            return min(batteries)

        batteries.sort()
        main = batteries[-n:]
        rest = sum(batteries[:-n])

        # distribute rest evenly over n batteries
        for i in range(len(main) - 1):
            d = main[i + 1] - main[i]
            need = d * (i + 1)

            if need > rest:
                x = rest // (i + 1)
                for j in range(i + 1):
                    main[j] += x
                    rest -= x
                break

            rest -= need
            for j in range(i + 1):
                main[j] = main[i + 1]

        # distribute rest evenly
        d, m = divmod(rest, len(main))
        for j in range(len(main)):
            main[j] += d

        # useless, just for beauty
        main[-1] += m

        return min(main)

