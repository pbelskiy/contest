class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longest_idx = events[0][0]
        longest_time = events[0][1]

        prev = events[0][1]
        for idx, time in events[1:]:
            d = time - prev

            if d == longest_time:
                longest_idx = min(longest_idx, idx)

            if d > longest_time:
                longest_time = d
                longest_idx = idx

            prev = time

        return longest_idx
