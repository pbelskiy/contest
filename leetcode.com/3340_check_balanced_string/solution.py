class Solution:
    def isBalanced(self, num: str) -> bool:
        a = sum(int(num[i]) for i in range(0, len(num), 2))
        b = sum(int(num[i]) for i in range(1, len(num), 2))

        return a == b
