class Solution:
    def reorganizeString(self, s: str) -> str:
        res, count, t = '', Counter(s), 0

        while t < len(s):
            add = False

            for k, v in count.most_common():
                if v <= 0:
                    continue

                if not res or res[-1] != k:
                    res += k
                    count[k] -= 1
                    t += 1
                    add = True
                    break

            if not add:
                return ''

        return res
