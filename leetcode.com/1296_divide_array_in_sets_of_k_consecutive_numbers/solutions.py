class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        h = list(count.keys())
        heapify(h)

        while h:
            if len(h) < k:
                return False

            p = None
            r = []
            for _ in range(k):
                v = heappop(h)

                if p is not None and v - 1 != p:
                    return False
                p = v

                count[v] -= 1
                if count[v] > 0:
                    r.append(v)
                else:
                    del count[v]

            for v in r:
                heappush(h, v)

        return True
