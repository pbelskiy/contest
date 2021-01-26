class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = [int(i) for i in str(int(''.join(map(str, digits))) + 1)]

        for _ in range(len(digits) - len(r)):
            r.insert(0, 0)

        return r


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + 1 <= 9:
                digits[i] += 1
                break

            digits[i] = 0

            if i == 0:
                digits.insert(0, 1)
                break

        return digits
