class Solution:
    def hIndex(self, citations: List[int]) -> int:
        last = 0

        for i in range(len(citations)):
            t = sum(citations[j] >= i + 1 for j in range(len(citations)))
            if i + 1> t:
                break

            last = i + 1

        return last
