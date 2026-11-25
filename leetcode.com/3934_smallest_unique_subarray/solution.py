# bisect over rolling hash
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        BASE = max(nums)

        # есть ли окно шириной k
        def rolling_hash(k): 
            h, cnt = 0, Counter()

            # наращиваем первичное окно
            for i in range(k):
                h += nums[i] * pow(BASE, k - i - 1, MOD)
            h %= MOD
            cnt[h] += 1

            # двигаем окно
            left, right = 0, k

            x = pow(BASE, k - 1, MOD)
            while right < len(nums):
                h -= (nums[left] * x)
                h *= BASE
                h += (nums[right])

                h %= MOD

                left += 1
                right += 1

                cnt[h] += 1

            if 1 in cnt.values():
                return True

            return False

        lo, hi = 1, len(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if rolling_hash(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo

