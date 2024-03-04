class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort()
        score = 0
        best = 0

        left, right = 0, len(tokens) - 1

        while True:
            # get tokens
            while left < len(tokens):
                if tokens[left] > power:
                    break
                power -= tokens[left]
                score += 1
                left += 1

            best = score

            # get power
            if right <= left or score == 0:
                break

            power += tokens[right]
            score -= 1
            right -= 1

        return best
