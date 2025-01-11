"""
Calculate number of each character occurance.

Calculate minimum posssible count of palindromes we
can construct from it.

If minimum lower than k, then we can increase count
of palindromes reducing character from palindromes
constructed above.

TC: O(N)
SC: O(1)
"""
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        count = Counter(s)

        # calculate minimum possible palindromes
        minimum = len([v for v in count.values() if v % 2])

        # at least we can cunstruct 1 from even count
        if minimum == 0:
            minimum = 1

        if minimum > k:
            return False

        # then step by step get characters from palindromes above
        return True
