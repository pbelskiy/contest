"""
Brute force, build new strs column by column.
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        def add_index(arr, i):
            b = []
            for j in range(len(strs)):
                if not arr:
                    b.append(strs[j][i])
                else:
                    b.append(arr[j] + strs[j][i])

            return b

        t = 0
        r = [] 
        for i in range(len(strs[0])):
            b = add_index(r, i)
            print(r, b)

            if sorted(b) != b:
                continue

            # add new index if it will no break
            r = b
            t += 1

        return len(strs[0]) - t

