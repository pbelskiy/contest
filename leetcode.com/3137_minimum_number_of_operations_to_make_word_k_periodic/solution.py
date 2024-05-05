"""
Collect count of each chunk from word, the most common one will be
our target, so the count of rest chunks is result.

TC: O(sort)
SC: O(N)
"""
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        count = Counter(word[i:i+k] for i in range(0, len(word), k))
        return sum(v for _, v in list(count.most_common())[1:])
