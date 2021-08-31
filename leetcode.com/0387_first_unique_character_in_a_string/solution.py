class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        index = 10**6

        for ch, n in count.items():
            if n == 1:
                index = min(index, s.find(ch))

        if index == 10**6:
            return -1

        return index
