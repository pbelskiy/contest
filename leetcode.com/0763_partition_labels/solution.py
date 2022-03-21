class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        parts = []

        limit = -1
        right = -1
        while limit < len(s) - 1:
            start = limit + 1
            left = start
            limit = start + 1

            while left < limit:
                right = len(s) - 1

                while right > limit and s[left] != s[right]:
                    right -= 1

                limit = right
                left += 1

            if limit - start == 1 and s[start] != s[limit]:
                limit -= 1

            parts.append(limit - start + 1)

        return parts
