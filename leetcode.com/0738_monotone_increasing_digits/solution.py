class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        number = list(map(int, list(str(n))))
        length = len(number)

        while True:
            bad = False
            for i in range(length - 1):
                if number[i] <= number[i + 1]:
                    continue


                number[i] -= 1

                for j in range(i + 1, length):
                    number[j] = 9

                bad = True
                break

            if bad is False:
                return ''.join(map(str, number)).lstrip('0')
