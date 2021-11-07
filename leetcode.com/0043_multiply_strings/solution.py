class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def atoi(s) -> int:
            n = 0
            for i, ch in enumerate(reversed(s)):
                n += (ord(ch) - ord('0')) * 10**i
            return n

        # atoi & multiply
        n = atoi(num1) * atoi(num2)

        # itoa
        arr = []
        while True:
            arr.append(chr(ord('0') + n % 10))
            n //= 10

            if n == 0:
                break

        return ''.join(arr[::-1])
