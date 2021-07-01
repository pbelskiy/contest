from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(2**n)]

        values = list(range(2**n))
        count = len(values)

        for i in range(1, count):
            for j in range(i, count):
                if bin(values[i] ^ values[j]).count('1') != 1:
                    continue

                if j - i > 1:
                    values[i+1], values[j] = values[j], values[i+1]
                break

        return values


values = Solution().grayCode(5)

for n1, n2 in zip(values, values[1:]):
    print(n1, n2, bin(n1 ^ n2).count('1'))
