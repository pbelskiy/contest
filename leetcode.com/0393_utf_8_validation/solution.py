class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def bit(n):
            return bin(n)[2:].rjust(8, '0')

        def follow(i, n):
            if i + n > len(data):
                return False

            for j in range(i, i + n):
                if not bit(data[j]).startswith('10'):
                    return False

            return True

        def check(i):
            if i >= len(data):
                return True

            if bit(data[i]).startswith('0'):
                return check(i + 1)

            if bit(data[i]).startswith('110') and follow(i + 1, 1):
                return check(i + 2)

            if bit(data[i]).startswith('1110') and follow(i + 1, 2):
                return check(i + 3)

            if bit(data[i]).startswith('11110') and follow(i + 1, 3):
                return check(i + 4)

            return False

        return check(0)
