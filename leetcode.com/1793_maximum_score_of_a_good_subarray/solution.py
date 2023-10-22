class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = k
        j = k
        m = nums[k]
        best = m

        while True:

            # choce from left or right side
            if i - 1 >= 0 and j + 1 < len(nums):
                if nums[i - 1] >= nums[j + 1]:
                    m = min(m, nums[i - 1])
                    i -= 1
                else:
                    m = min(m, nums[j + 1])
                    j += 1

            # go left only possible
            elif i - 1 >= 0:
                m = min(m, nums[i - 1])
                i -= 1

            # go right only possible
            elif j + 1 < len(nums):
                m = min(m, nums[j + 1])
                j += 1

            else:
                break

            best = max(best, (j - i + 1)*m)

        return best
