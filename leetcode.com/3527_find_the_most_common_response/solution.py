"""
Just use set and then sort the results.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        f = Counter()

        for resp in responses:
            f.update(Counter(set(resp)))

        a = sorted(f.items(), key=lambda t: (-t[1], t[0], len(t[0])))
        return a[0][0]

