class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def get_factors(n):
            f = []

            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    f.extend([i, n // i])

            return set(f)

        for i in range(len(nums2)):
            nums2[i] *= k

        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)

        t = 0
        for k, v in cnt1.items():
            t += sum(cnt2[f] for f in get_factors(k))*v

        return t
