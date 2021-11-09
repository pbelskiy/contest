class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        def get_mask(s):
            mask = 0
            for ch in s:
                mask |= (1 << (ord(ch) - ord('a')))
            return mask

        cnt = Counter()
        for w in words:
            cnt[get_mask(w)] += 1

        intersections = []

        for puzzle in puzzles:
            # try all possible puzzle masks
            first = get_mask(puzzle[0])
            total = cnt[first]

            mask = get_mask(puzzle[1:])
            submask = mask
            while submask:
                total += cnt[first | submask]
                submask = (submask - 1) & mask
                # print(bin(submask))

            intersections.append(total)

        return intersections
