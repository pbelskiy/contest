class Solution:
    def minSwaps(self, s: str) -> int:
        count = Counter(s)

        if abs(count['0'] - count['1']) > 1:
            return -1

        # construct `alternating` strings
        if len(s) % 2 == 0:
            s1 = '01'*(len(s) // 2)
            s2 = '10'*(len(s) // 2)
        elif count['0'] > count['1']:
            s1 = s2 = '01'*(len(s) // 2) + '0'
        else:
            s1 = s2 = '10'*(len(s) // 2) + '1'

        # compare input to `alternating` strings above
        l1, l2 = 0, 0
        for a, b, c in zip(s, s1, s2):
            if a != b:
                l1 += 1
            if a != c:
                l2 += 1

        return min(l1, l2) // 2
