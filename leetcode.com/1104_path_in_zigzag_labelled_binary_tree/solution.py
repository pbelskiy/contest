class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        rev = False
        depth = 0
        levels = []

        while True:
            level = [2**depth + i for i in range(2**depth)]
            if rev:
                level = level[::-1]
            depth += 1
            rev = not rev

            levels.append(level)
            if  label in level:
                break

        res = []
        i = len(levels) - 1
        index = levels[i].index(label)
        while i >= 0:
            res.append(levels[i][index])
            i -= 1
            index //= 2

        return res[::-1]
