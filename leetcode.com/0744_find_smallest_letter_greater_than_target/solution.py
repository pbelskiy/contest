class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect(letters, target)
        if i >= len(letters):
            i = 0
        return letters[i]
