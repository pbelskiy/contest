class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        def sliding_window(left):
            count = Counter(words)
            for right in range(left, len(s), width):
                # get current substring
                ss = s[right:right+width]

                # move left pointer
                while count[ss] == 0 and left <= right:
                    count[s[left:left+width]] += 1
                    left += width

                if count[ss] > 0:
                    count[ss] -= 1

                # update indices
                if sum(count.values()) == 0:
                    indices.append(left)

        indices = []
        width = len(words[0])
        for w in range(width):
            sliding_window(w)
        return sorted(indices)
