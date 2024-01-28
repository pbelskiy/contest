"""
1) Brute force solution is like this: O(N^2):
```
    t = 0

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (x + y) % 2 == 1:
                t += 1

    return t
```

Can be esily optimized to O(N):
```
    for x in range(1, n + 1):
        if x % 2 == 1:
            t += m // 2
        elif m % 2 == 1:
            t += (m // 2) + 1
        else:
            t += m // 2
```

"""
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        t = 0

        for x in range(1, n + 1):
            if x % 2 == 1:
                t += m // 2
            elif m % 2 == 1:
                t += (m // 2) + 1
            else:
                t += m // 2

        return t
