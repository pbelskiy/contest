"""
Greedy

TC: O(N)
SC: O(N)
"""
class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        count = Counter(t)

        r = ''
        for ch in s:
            if ch == '1':
                if count['0'] > 0:
                    r += '1'
                    count['0'] -= 1
                else:
                    r += '0'
                    count['1'] -= 1
            else:
                if count['1'] > 0:
                    r += '1'
                    count['1'] -= 1
                else:
                    r += '0'
                    count['0'] -= 1 

        return r

