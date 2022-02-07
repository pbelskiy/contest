class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return (collections.Counter(t) - collections.Counter(s)).most_common(1)[0][0]
