class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        total = 0

        deliciousness.sort()
        count = Counter(deliciousness)
        powers = [2**p for p in range(22)]

        for n, v in count.items():
            for p in powers:
                d = p - n
                if d < n:
                    continue

                if n == d and count[d] > 1:
                    с = count[n] - 1
                    total += ((с + 1) * с) // 2  # arithmetic progression

                elif n != d and count[d] > 0:
                    total += count[n] * count[d]

                total %= (10**9 + 7)

        return total
