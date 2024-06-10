class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        p = None

        for t in s.split(' '):
            if t.isnumeric():
                if p is None:
                    p = int(t)
                elif int(t) <= p:
                    return False

                p = int(t)

        return True
