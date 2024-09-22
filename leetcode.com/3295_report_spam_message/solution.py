class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        s = set(bannedWords)
        t = 0

        for m in message:
            if m in s:
                t += 1

            if t > 1:
                return True

        return False
