class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        count = Counter()
        sizes = []

        for w in words:
            count.update(w)
            sizes.append(len(w))

        a = []
        for _, v in count.items():
            a.append(v)

        a.sort()

        total = 0
        for s in sorted(sizes):
            # find one odd
            if s % 2 == 1:
                # try to find among odd numbers
                for i in range(len(a)):
                    if a[i] % 2 == 1:
                        a[i] -= 1
                        s -= 1
                        break

                # try to find among even numbers
                if s % 2 == 1:
                    for i in range(len(a)):
                        if a[i] % 2 == 0:
                            a[i] -= 1
                            s -= 1
                            break

            # and rest one by one of even numbers
            if s > 0:
                for i in range(len(a)):
                    if a[i] < 2:
                        continue

                    m = min(s, a[i]) & ~1

                    s -= m
                    a[i] -= m

                    if s == 0:
                        break

            if s == 0:
                total += 1

            a = sorted(filter(lambda v: v > 0, a))

        return total
