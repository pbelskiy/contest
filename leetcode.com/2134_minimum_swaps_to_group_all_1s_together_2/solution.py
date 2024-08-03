class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        t = nums.count(1)
        a = nums*2

        left = 0
        count = Counter(a[:t])
        best = float("inf")

        for right in range(t, len(a)):
            best = min(best, count[0])

            count[a[right]] += 1
            count[a[left]] -= 1
            left += 1


        return best
