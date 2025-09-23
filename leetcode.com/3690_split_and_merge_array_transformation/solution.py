class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        q = deque([(tuple(nums1), 0)])
        v = {tuple(nums1)} 

        while q:
            t, m = q.popleft()
            if t == tuple(nums2):
                return m

            for l in range(len(t)):
                for r in range(l + 1, len(t) + 1):
                    a = t[:l] + t[r:]
                    b = t[l:r]

                    for i in range(len(a) + 1):
                        c = a[:i] + b + a[i:]
                        if c not in v:
                            v.add(c)
                            q.append((c, m + 1))

