import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = re.sub(r'\W+', '', s.lower().replace('_', ''))
        return ns == ns[::-1]
