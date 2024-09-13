class Solution:
    def countPairs(self, nums: List[int]) -> int:

        def is_equal(a, b):
            d = abs(len(a) - len(b))

            if len(a) < len(b):
                a = '0'*d + a
            elif len(b) < len(a):
                b = '0'*d + b

            if set(a) != set(b):
                return False

            arr1, arr2 = [], []
            for x, y in zip(a, b):
                if x != y:
                    arr1.append(x)
                    arr2.append(y)

                if len(arr1) > 2:
                    return False

            return sorted(arr1) == sorted(arr2)

        t = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if is_equal(str(nums[i]), str(nums[j])):
                    t += 1

        return t
