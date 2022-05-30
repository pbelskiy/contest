class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(map(int, num))

        for i in range(len(num)):
            if count[i] != int(num[i]):
                return False

        return True
