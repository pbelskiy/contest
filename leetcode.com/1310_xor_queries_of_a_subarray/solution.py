class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        s, prefix = 0, []
        for n in arr:
            s ^= n
            prefix.append(s)

        res = []
        for left, right in queries:

            if left == 0:
                v = prefix[right]
            else:
                v = prefix[right] ^ prefix[left - 1]

            res.append(v)

        return res
