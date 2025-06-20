class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:

        @cache
        def mul(m):
            v = 1
            for i in range(len(nums)):
                if (1 << i) & m:
                    v *= nums[i]
            return v

        @cache
        def dfs(m1, m2):
            if mul(m1) > target or mul(m2) > target:
                return False

            f = False

            for i in range(len(nums)):
                if (1 << i) & m1:
                    continue
                if (1 << i) & m2:
                    continue

                f = True

                # add to first
                if dfs(m1 | (1 << i), m2):
                    return True

                # add to second
                if dfs(m1, m2 | (1 << i)):
                    return True

            if not f and mul(m1) == mul(m2) == target:
                return True

            return False

        if mul(-1) < target:
            return False

        if mul(-1) % target != 0:
            return False

        return dfs(0, 0)

