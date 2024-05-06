class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def has_cycle(i):
            count = Counter()

            while True:
                count[i] += 1

                i = g.get(i)
                if i is None:
                    return False

                if count[i] > 1:
                    break

            v = sorted(nums[k] for k, v in count.items() if v > 1)

            if len(v) <= 1:
                return False

            if v[0] >= 0 and v[-1] >= 0:
                return True

            if v[0] < 0 and v[-1] < 0:
                return True

            return False

        g = {}
        for i in range(len(nums)):
            g[i] = (i + nums[i]) % len(nums)

        for i in range(len(nums)):
            if has_cycle(i):
                return True

        return False
