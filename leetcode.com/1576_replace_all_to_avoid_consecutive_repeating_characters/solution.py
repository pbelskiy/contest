class Solution:
    def modifyString(self, s: str) -> str:
        a = list(s)

        for i in range(len(a)):
            if a[i] != '?':
                continue

            used = set()
            if i > 0:
                used.add(a[i - 1])
            if i + 1 < len(s):
                used.add(a[i + 1])

            a[i] = next(iter(set(string.ascii_lowercase) - set(used)))

        return ''.join(a)
