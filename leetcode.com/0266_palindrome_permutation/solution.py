class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter([v % 2 for v in Counter(s).values()])

        if count[1] > 1:
            return False

        return True
