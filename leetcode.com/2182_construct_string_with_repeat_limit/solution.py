class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        h = []
        for ch, n in Counter(s).items():
            heappush(h, (-ord(ch), n))

        s = ''
        used = Counter()
        while h:
            x, n = heappop(h)

            # already used, try other char
            if used[x] >= repeatLimit:
                if not h:
                    break
                xp, np = x, n
                used.clear()
                x, n = heappop(h)
                heappush(h, (xp, np))

            used = Counter({x: used[x]})

            s += chr(-x)
            n -= 1
            used[x] += 1
            if n > 0:
                heappush(h, (x, n))

        return s
