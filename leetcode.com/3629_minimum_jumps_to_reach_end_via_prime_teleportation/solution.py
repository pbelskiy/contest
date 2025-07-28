class Solution:
    def minJumps(self, nums: List[int]) -> int:

        def get_primes(count):
            if count < 2:
                return set()

            is_prime = [True] * (count + 1)
            is_prime[0] = is_prime[1] = False

            p = 2
            while (p * p <= count):
                if is_prime[p]:
                    for i in range(p * p, count + 1, p):
                        is_prime[i] = False
                p += 1

            return set([p for p in range(2, count + 1) if is_prime[p]])

        m = max(nums)
        p = get_primes(m)
        d = defaultdict(list)

        # collect indices
        for i, n in enumerate(nums):
            d[n].append(i)

        indices_map = {}
        for i in range(len(nums)):
            if nums[i] not in p:
                continue
            if nums[i] in indices_map:
                continue

            indices = []
            f = nums[i]
            x = f
            while x <= m:
                if x in d:
                    indices.extend(d[x])
                x += f

            indices_map[nums[i]] = indices

        # bfs
        q = [(0, 0, 0)]
        v = defaultdict(lambda: float('inf'))
        while q:
            j, dist, i = heappop(q)
            # print(j, i, len(q))

            if j > v[i]:
                continue

            if i == len(nums) - 1:
                return j

            if i - 1 >= 0 and j + 1 < v[i - 1]:
                v[i - 1] = j + 1
                heappush(q, (j + 1, abs(len(nums) - i + 1), i - 1))

            if i + 1 < len(nums) and j + 1 < v[i + 1]:
                v[i + 1] = j + 1
                heappush(q, (j + 1, abs(len(nums) - i + 1), i + 1))

            if nums[i] not in p:
                continue

            for ii in indices_map[nums[i]]:
                if j + 1 < v[ii]:
                    v[ii] = j + 1
                    heappush(q, (j + 1, abs(len(nums) - ii), ii))
            indices_map[nums[i]] = []

        return -1

