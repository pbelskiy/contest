class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s = set()

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if i == j:
                    continue

                for k in range(len(digits)):
                    if k == j or i == k or digits[k] % 2 == 1:
                        continue

                    s.add(str(digits[i]) + str(digits[j]) + str(digits[k]))

        return len(s)
