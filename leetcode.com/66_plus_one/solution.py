class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = [int(i) for i in str(int(''.join(map(str, digits))) + 1)]

        for _ in range(len(digits) - len(r)):
            r.insert(0, 0)

        return r

