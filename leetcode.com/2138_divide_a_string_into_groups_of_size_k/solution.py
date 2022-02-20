class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups = []

        for i in range(len(s) // k):
            groups.append(s[i*k:(i+1)*k])

        f = len(s) % k

        if f:
            groups.append(s[-f:] + fill*(k - f))

        return groups
