class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []

        while columnNumber > 0:
            a = columnNumber // 26
            b = columnNumber % 26

            if b == 0:
                a -= 1
                b = 26

            title.insert(0, chr(ord('A') - 1 + b))
            columnNumber = a

        return ''.join(title)
