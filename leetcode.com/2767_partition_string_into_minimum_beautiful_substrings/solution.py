class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:

        def dfs(string):
            # it doesn't contain leading zeros
            if s[0] == '0':
                return float('inf')

            # it's the binary representation of a number that is a power of 5
            best = float('inf')
            for power in [bin(5**n)[2:] for n in range(10, -1, -1)]:
                total = string.count(power)
                if total == 0:
                    continue

                for substring in filter(None, string.split(power)):
                    total += dfs(substring)

                best = min(best, total)

            return best

        result = dfs(s)
        if result == float('inf'):
            return -1

        return result
