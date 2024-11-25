class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], prevCost: List[int]) -> int:
        r = 0

        for a, b in zip(s, t):
            if a == b:
                continue

            start = ord(a) - ord('a')
            end = ord(b) - ord('a')

            diff_forw = (end - start) % 26
            diff_back = (start - end) % 26

            forward_cost = sum(nextCost[(start + i) % 26] for i in range(diff_forw))
            backward_cost = sum(prevCost[(start - i) % 26] for i in range(diff_back))

            r += min(forward_cost, backward_cost)

        return r
