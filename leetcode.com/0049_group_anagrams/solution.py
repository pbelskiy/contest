class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for a in strs:
            d[frozenset(collections.Counter(a).items())].append(a)

        return d.values()
