class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        m = 0

        for k in nums:
            if k in visited:
                continue

            l = []

            nm = 0
            while True:
                n = nums[k]
                if n in visited:
                    break

                nm += 1
                visited.add(n)
                k = n

            m = max(m, nm)

        return m
