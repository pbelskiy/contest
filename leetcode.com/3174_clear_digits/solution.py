class Solution:
    def clearDigits(self, s: str) -> str:
        a = list(s)

        found = True
        while found:
            found = False
            for i in range(len(a)):
                if a[i].isdigit():
                    a[i] = '@'
                    found = True
                    for j in range(i - 1, -1, -1):
                        if a[j] != '@' and not a[j].isdigit():
                            a[j] = '@'
                            break

        return ''.join(filter(lambda ch: ch != '@', a))
