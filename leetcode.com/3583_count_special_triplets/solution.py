class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ft = Counter(nums)
        fc = Counter()

        t = 0
        for n in nums:
            need = n*2
            if fc[need] == 0:
                fc[n] += 1
                continue

            forward = ft[need] - fc[need]
            if n == need:
                forward -= 1

            # print('Current:', n, 'before:', fc[need], forward)
            t += fc[need] * forward
            fc[n] += 1

        return t % (10**9 + 7)

