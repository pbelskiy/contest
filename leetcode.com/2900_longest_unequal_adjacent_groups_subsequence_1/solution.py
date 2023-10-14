"""
Here we need calc length of alternating values.

In description we see "Note: strings in words may be unequal in length."
But it doesn't matter, it note just for confuse you.


TC: O(N)
SC: O(N)
"""
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        arr, last = [0], groups[0]

        for i in range(n):
            if groups[i] != last:
                arr.append(i)
                last = groups[i]

        return [words[i] for i in arr]
