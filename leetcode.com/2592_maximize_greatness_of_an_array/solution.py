class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        arr = sorted(count.keys())

        t = 0
        for n in nums:
            i = bisect.bisect(arr, n)
            while i < len(arr):
                n = arr[i]
                if count[n] > 0:
                    count[n] -= 1

                    # next bisect optimization
                    if count[n] == 0:
                        if i > 0:
                            arr[i] = arr[i - 1]
                        else:
                            arr[i] = 0

                    t += 1
                    break

                i += 1

        return t
