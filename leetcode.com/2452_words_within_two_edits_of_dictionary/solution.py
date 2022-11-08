class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        def get_diff(s1, s2):
            count = 0

            for ch1, ch2 in zip(s1, s2):
                if ch1 != ch2:
                    count += 1

            return count

        arr = []

        for q in queries:
            for d in dictionary:
                if get_diff(q, d) <= 2:
                    arr.append(q)
                    break

        return arr
