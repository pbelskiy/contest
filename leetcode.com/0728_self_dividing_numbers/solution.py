class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []

        for n in range(left, right + 1):
            for i in map(int, list(str(n))):
                if i == 0:
                    break

                if n % i != 0:
                    break
            else:
                l.append(n)

        return l
