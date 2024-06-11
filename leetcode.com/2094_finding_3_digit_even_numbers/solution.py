class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        u = []
        count = Counter(digits)

        for n in range(100, 999, 2):
            for k, v in Counter(map(int, str(n))).items():
                if count[k] < v:
                    break
            else:
                u.append(n)

        return sorted(u)
