class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []

        for i in range(len(target)):
            s = res[-1] if res else ''
            for j in range(ord('a'), ord(target[i]) + 1):
                res.append(s + chr(j))

        return res
