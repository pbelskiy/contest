class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        af = lambda a, b: int((k / 2) * (a + b))

        result = []

        sa = sorted(nums[:k])
        cs = sum(sa)

        if sa == nums[:k] and af(sa[0], sa[0] + k - 1) == cs:
            result.append(sa[-1])
        else:
            result.append(-1)

        left = 0
        for right in range(k, len(nums)):
            cs -= nums[left]
            cs += nums[right]

            left += 1

            if nums[right] - 1 != nums[right - 1]:
                result.append(-1)
                continue

            if af(nums[left], nums[left] + k - 1) != cs:
                result.append(-1)
                continue

            result.append(nums[right])

        return result
