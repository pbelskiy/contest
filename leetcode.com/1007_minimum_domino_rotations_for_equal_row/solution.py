class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cnt_1 = collections.Counter(tops)
        cnt_2 = collections.Counter(bottoms)

        minimum = float('inf')

        for v, n in cnt_1.most_common():
            if n == len(tops):
                return 0

            if n + cnt_2[v] < len(tops):
                continue

            s1, s2 = 0, 0

            for i in range(len(tops)):

                if tops[i] != v and bottoms[i] == v:
                    s1 += 1

                if tops[i] == v and bottoms[i] != v:
                    s2 += 1

            if s1 + cnt_1[v] == len(tops) or s2 + cnt_2[v] == len(tops):
                total = min(s1, s2)
                minimum = min(minimum, total)

        if minimum == float('inf'):
            return -1

        return minimum
