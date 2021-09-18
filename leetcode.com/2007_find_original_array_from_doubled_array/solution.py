class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        original = []
        numbers = collections.Counter(changed)

        for n in sorted(changed):
            v = n*2
            if numbers.get(n, 0) > 0 and numbers.get(v, 0) > 0:
                original.append(n)
                numbers[n] -= 1
                numbers[v] -= 1
            elif n // 2 not in numbers or n % 2 == 1:
                return []

        return original
